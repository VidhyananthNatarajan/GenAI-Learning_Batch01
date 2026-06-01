from textblob import TextBlob

# Sample Feedback
#feedback ="I used this product. I am very much satisfied with the product with the way how it works."
feedback ="I used this product. I am totally frustated with the product with the way how it works.It's total waste of buying."
# Create a TextBlob object
blob = TextBlob(feedback)

# Perform Sentiment Analysis
sentiment = blob.sentiment

# Polarity - Measure of sentiment's from positivity to negativity (-1 -> Negative, 0- neutral, 1- Positive)
# Subjectivity - Paritioning the feeback either as objective or subjective (0 -Objective ,1 - Subjective)

print(f"The Polarity value is:{sentiment.polarity}")
print(f"The Subjectivity value is:{sentiment.subjectivity}")
