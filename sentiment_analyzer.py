from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(title):
    score = analyzer.polarity_scores(title)['compound']
    impact = "⚠️ High Impact" if abs(score) > 0.6 else "Medium Impact" if abs(score) > 0.4 else "Low"
    return score, impact
