"""
Custom prompt templates for LightRAG response types.
This file extends the default prompts in prompt.py with more detailed instructions
for each response type.
"""

from typing import Dict, Any

# Define detailed instructions for each response type
RESPONSE_TYPE_INSTRUCTIONS: Dict[str, str] = {
    "Multiple Paragraphs": """
- Structure your response in multiple paragraphs with clear topic sentences
- Use 3-5 paragraphs to cover different aspects of the answer
- Include transitions between paragraphs for smooth flow
- Keep paragraphs focused on a single main idea
- Use markdown formatting for emphasis where appropriate
- Keep the total length under 1000 words
    """,
    
    "Single Paragraph": """
- Provide a concise, comprehensive answer in a single paragraph
- Include the most important information only
- Use clear, direct language
- Keep the total length under 300 words
    """,
    
    "Bullet Points": """
- Structure your response as a list of bullet points
- Use 5-10 bullet points to cover key information
- Start each bullet with a clear, informative phrase
- Keep bullet points concise (1-2 sentences each)
- Use sub-bullets for supporting details if needed
- Use markdown bullet point formatting
    """,
    
    "Table Format": """
- Present information in a markdown table format
- Include a header row with clear column names
- Organize data logically with appropriate columns
- Use 3-7 columns depending on the data complexity
- Include 5-10 rows of relevant information
- Align numeric data to the right, text to the left
- Add a brief explanation before the table if needed
    """,
    
    "Step-by-Step Guide": """
- Structure as a sequential guide with numbered steps
- Include 5-10 steps to complete the process or understand the concept
- Start with an introduction explaining the goal
- Make each step clear, actionable, and self-contained
- Use imperative language for instructions
- Include a brief explanation with each step if needed
- Add a conclusion summarizing the process
- Use markdown formatting for step numbers
    """,
    
    "Short Report": """
- Structure as a brief professional report with 3 sections
- Include a "Summary" section (1-2 paragraphs)
- Include a "Key Findings" section (2-3 paragraphs or 3-5 bullet points)
- Include a "Conclusion" section (1 paragraph)
- Keep the total length under 1500 words
- Use markdown headings for each section
    """,
    
    "Detailed Report": """
- Structure as a comprehensive formal report with 5+ sections
- Include an "Executive Summary" (1-2 paragraphs)
- Include "Background/Context" section
- Include "Analysis" section with subsections as needed
- Include "Findings" section with detailed evidence
- Include "Knowledge Gap" section with discussion of gaps in knowledge
- Include "Recommendations" or "Conclusions" section
- Use proper markdown formatting with hierarchical headings
- Include relevant details from all provided sources
- Keep the total length under 3000 words
- Add a "References" section citing all sources used
    """,
    
    "Technical Documentation": """
- Structure as technical documentation with clear sections
- Begin with a "Purpose" section explaining the topic
- Include "Technical Details" section with precise information
- Add "Implementation" section with examples if applicable
- Include "Notes" or "Considerations" section for edge cases
- Use code blocks with appropriate syntax highlighting if relevant
- Use technical terminology appropriate to the domain
    """,
    
    "FAQ Format": """
- Structure as a series of questions and answers
- Begin with a brief introduction to the topic
- Format each Q&A pair with the question in bold
- Provide concise but complete answers to each question
- Cover 5-8 most relevant questions based on the query
- Organize questions in logical order of importance
    """,
    
    "Comparative Analysis": """
- Structure as a comparison between multiple items, concepts, or approaches
- Begin with an introduction explaining the comparison criteria
- Include a section for each item being compared
- Use a consistent structure for each comparison section
- Include a "Similarities" section highlighting common features
- Include a "Differences" section highlighting distinguishing features
- End with a "Recommendation" or "Conclusion" section
- Use tables or bullet points for direct comparisons where appropriate
- Keep analysis balanced and objective
    """
}

def get_response_type_instructions(response_type: str) -> str:
    """
    Get the detailed instructions for a specific response type.
    
    Args:
        response_type: The name of the response type
        
    Returns:
        Detailed formatting instructions for the specified response type
    """
    return RESPONSE_TYPE_INSTRUCTIONS.get(
        response_type, 
        "Provide a clear, concise response in an appropriate format."
    )
