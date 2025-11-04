def print_banner():
    print("==============================")
    print("Instagram Content Generator")
    print("==============================")


def get_user_input():
    strategy = input("Enter content strategy: ")
    return strategy


def display_results(results):
    print("Generated Instagram Content:")
    for result in results:
        print(f"- {result}")


def main():
    print_banner()
    strategy = get_user_input()
    # Placeholder: Replace with actual content generation logic
    results = [f"Content Idea {i + 1} based on {strategy}" for i in range(5)]
    display_results(results)
    save_option = input("Do you want to save results to file? (yes/no): ").strip().lower()
    if save_option == 'yes':
        with open('instagram_content.txt', 'w') as f:
            for result in results:
                f.write(result + '\n')
        print("Results saved to 'instagram_content.txt'")
    else:
        print("Results not saved.")


if __name__ == '__main__':
    main()