from datetime import datetime

from tradingagents.default_config import DEFAULT_CONFIG
from tradingagents.graph.trading_graph import TradingAgentsGraph

config = DEFAULT_CONFIG.copy()

print("=" * 60)
print("            XAUUSD AI TERMINAL")
print("=" * 60)

ta = TradingAgentsGraph(debug=True, config=config)

while True:

    print("\nChoose an option:")
    print("1. Analyze XAUUSD")
    print("2. Multi-Timeframe Analysis")
    print("3. Create Trading Plan")
    print("0. Exit")

    choice = input("\nEnter choice: ").strip()

    if choice == "0":
        print("Goodbye!")
        break

    date = input(
        f"Enter Date (YYYY-MM-DD) [Press Enter for Today {datetime.today().strftime('%Y-%m-%d')}]: "
    ).strip()

    if date == "":
        date = datetime.today().strftime("%Y-%m-%d")

    symbol = "GC=F"

    print("\nPlease wait... AI is analyzing Gold.\n")

    try:

        if choice == "1":

            _, result = ta.propagate(symbol, date)

            print("\n==============================")
            print("XAUUSD ANALYSIS")
            print("==============================")
            print(result)

        elif choice == "2":

            print("\nRunning Multi-Timeframe Analysis...\n")

            _, result = ta.propagate(symbol, date)

            print("\n==============================")
            print("MULTI-TIMEFRAME ANALYSIS")
            print("==============================")
            print(result)

        elif choice == "3":

            print("\nCreating Trading Plan...\n")

            _, result = ta.propagate(symbol, date)

            print("\n==============================")
            print("TODAY'S TRADING PLAN")
            print("==============================")
            print(result)

        else:
            print("Invalid option.")

    except Exception as e:
        print("\nError:")
        print(e)