from coordinator import run_pipeline

if __name__ == "__main__":
    print("🛠️ Welcome to CircularAgent: Sustainable Manufacturing Advisor 🛠️\n")
    user_query = input("Describe your manufacturing sustainability goal:\n> ")

    # Run the full pipeline with smarter planning and smarter insights
    final_summary = run_pipeline(user_query)

    print("\n=== Sustainability Recommendations ===\n")
    print(final_summary)
