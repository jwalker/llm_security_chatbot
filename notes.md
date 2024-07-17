# Change the Context prompt to suit your needs
prompt_template = """
    Q: {user_query}
    Context: The user is conducting a detailed analysis of publicly traded companies, focusing on the financial stability, operational shifts, and cybersecurity postures by examining the 1.05 items in their 8-K and 10-K SEC filings. These filings are pivotal in understanding material changes in the companies' financial condition or operational strategies, including the critical aspect of cybersecurity risks and their management. The user objective is to ascertain how these changes, particularly cybersecurity issues, might influence the companies' future performance and stock valuation.
    1. Summarize any 1.05 items mentioned in the most recent 8-K and 10-K filings for [Company Name], with a special emphasis on cybersecurity-related disclosures. Highlight the nature of the material changes reported, including any cybersecurity incidents, data breaches, updates to cybersecurity policies, or investments in cybersecurity infrastructure.
    2. Compare these changes, with a focus on cybersecurity aspects, to those disclosed in the previous year's filings to identify trends, significant shifts in cybersecurity posture, financial health, or operational strategies.
    3. Analyze the potential implications of these cybersecurity-related changes on the company's future performance. Consider factors such as the company's resilience to cyber threats, market competitiveness, financial stability, and potential risks or opportunities arising from the cybersecurity landscape.
    4. Provide an advanced assessment of how these material changes, particularly those related to cybersecurity, could impact the company's stock valuation. Include any strategic recommendations for investors who consider cybersecurity a critical factor in their investment decisions.
    Ensure that your analysis accounts for the broader economic, technological, and industry-specific contexts that could influence the significance and implications of these cybersecurity-related changes. Your insights will help in making informed decisions about the financial viability and investment potential of these companies from a cybersecurity perspective.
    A: """

# run backend (must happen in backend directory)
python app.py

# run frontend (must happen in frontend directory)
npm run serve

# Frontend UI
http://127.0.0.1:8080

# When you hit send/submit sometimes it make take between 20-40 seconds to respond
# working on adding a loading / analyzing progress bar
# It would be a lot faster if I use just used subprocess directly to the LLM but..
# Lazy currently

# Curl history - currently saved as json file.
# Will implement LangChain later
curl http://127.0.0.1:5000/get_history

# Submit query via curl
curl -X POST http://127.0.0.1:5000/submit_query \
-H "Content-Type: application/json" \
-d '{"query":"What is AI?"}'

# Submit query using a payload.json file
# Example payload.json file
{
  "query": "What is SEC 8k and 10k used for?"
}
# curl with payload
curl -v -X POST http://127.0.0.1:5000/submit_query \
-H "Content-Type: application/json" \
-d @payload.json

