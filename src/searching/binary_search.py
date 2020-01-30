class BinarySearch:
    def binarySearch(self, item, items_list):
        result = -1
        index = len(items_list) // 2

        if items_list[0] == item:
            return 0

        if items_list[len(items_list) - 1] == item:
            return len(items_list) - 1

        while index != 0 and index != len(items_list) - 1:
            if items_list[index] == item:
                result = index
                break
            elif item < items_list[index]:
                index = index // 2
            else:
                index = (index + len(items_list)) // 2

        return result

def main():
    items_list = [1, 2, 3, 4, 5]
    item = 7

    bs = BinarySearch()
    result = bs.binarySearch(item, items_list)

    if result != -1:
        print(f"element found at index: {result}")
    else:
        print(f"item not found")

if __name__ == "__main__":
    main()
