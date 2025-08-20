from vending import VendingMachine

def main():
    # Initialize vending machine
    vm = VendingMachine()

    # Add items
    vm.add_item('Snickers Bar', 2, quantity=3)
    vm.add_item('Clif Bar', 2.75, 10)
    vm.add_item('Potato Chips', 1.50, 4)

    # Insert money
    vm.insert_money(5)

    # Purchase items
    vm.purchase('Potato Chips')
    vm.purchase('Snickers Bar')

    # List available items
    vm.list_items()

    # Output change
    vm.output_change()

    # View total sales
    print(f"Total sales: ${vm.get_total_sales()}")

    #View stats for the last 2 purchases
    vm.stats(2)

if __name__ == "__main__":
    main()

