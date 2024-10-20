from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Input, Button, Static
from tqdm import tqdm
import halal_stock
import asyncio

class StockCheckApp(App):
    CSS = """
    Container {
        layout: grid;
        grid-size: 2;
        grid-gutter: 1 2;
        padding: 1 2;
    }
    #result {
        height: auto;
        width: 100%;
        background: $surface;
        color: $text;
        padding: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Input(placeholder="Enter product name", id="product_input"),
            Button("Check Stock", variant="primary", id="check_button"),
            Static(id="result", expand=True)
        )
        yield Footer()

    async def on_mount(self) -> None:
        self.halal_stocks = []
        await self.fetch_stocks()

    async def fetch_stocks(self) -> None:
        result_widget = self.query_one("#result")
        result_widget.update("Fetching stocks... Please wait.")

        def scrape_with_progress():
            with tqdm(total=100, desc="Scraping stocks", unit="%") as pbar:
                for i in range(10):  # Simulate progress
                    asyncio.sleep(0.5)  # Simulate work
                    pbar.update(10)
                return halal_stock.scrape_halal_stocks()

        self.halal_stocks = await asyncio.to_thread(scrape_with_progress)
        result_widget.update("Stocks fetched successfully!")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "check_button":
            self.check_stock()

    def check_stock(self) -> None:
        product_name = self.query_one("#product_input").value.lower()
        matches = [stock for stock in self.halal_stocks if product_name in stock.lower()]
        result = "\n".join(matches) if matches else "No stock name found in list"
        self.query_one("#result").update(result)

if __name__ == "__main__":
    app = StockCheckApp()
    app.run()