import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for visualizations
plt.style.use('ggplot')
sns.set_palette('husl')

# Load the data with encoding
df = pd.read_csv('Instagram data.csv', encoding='latin1')

print("=== Instagram Content Analysis ===\n")

# 1. Overall Performance Metrics
print("1. Overall Performance:")
print("-----------------------")
print(f"Total Posts Analyzed: {len(df)}")
print(f"Average Impressions per Post: {df['Impressions'].mean():.0f}")
print(f"Average Likes per Post: {df['Likes'].mean():.0f}")
print(f"Average Comments per Post: {df['Comments'].mean():.0f}")
print(f"Average Saves per Post: {df['Saves'].mean():.0f}\n")

# 2. Engagement Analysis
print("2. Engagement Analysis:")
print("---------------------")
engagement_rate = (df['Likes'].sum() + df['Comments'].sum()) / df['Impressions'].sum() * 100
save_rate = df['Saves'].sum() / df['Impressions'].sum() * 100
print(f"Overall Engagement Rate: {engagement_rate:.2f}%")
print(f"Save Rate: {save_rate:.2f}%\n")

# 3. Traffic Sources
print("3. Traffic Sources:")
print("-----------------")
sources = ['From Home', 'From Hashtags', 'From Explore', 'From Other']
traffic = df[sources].sum()
total_traffic = traffic.sum()
for source in sources:
    percentage = (traffic[source] / total_traffic) * 100
    print(f"{source}: {percentage:.1f}%")
print()

# 4. Top Performing Posts
print("4. Top Performing Posts:")
print("----------------------")
top_posts = df.nlargest(5, 'Impressions')[['Impressions', 'Likes', 'Comments', 'Saves', 'Caption']]
for idx, post in top_posts.iterrows():
    print(f"\nPost {idx + 1}:")
    print(f"Impressions: {post['Impressions']}")
    print(f"Likes: {post['Likes']}")
    print(f"Comments: {post['Comments']}")
    print(f"Saves: {post['Saves']}")
    print(f"Caption: {post['Caption'][:100]}...")

# Visualizations
plt.figure(figsize=(15, 10))

# 1. Distribution of Impressions
plt.subplot(2, 2, 1)
sns.histplot(data=df, x='Impressions', bins=30)
plt.title('Distribution of Post Impressions')

# 2. Engagement Correlation
plt.subplot(2, 2, 2)
engagement_metrics = ['Likes', 'Comments', 'Shares', 'Saves', 'Impressions']
sns.heatmap(df[engagement_metrics].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Engagement Metrics Correlation')

# 3. Traffic Sources
plt.subplot(2, 2, 3)
traffic.plot(kind='pie', autopct='%1.1f%%')
plt.title('Traffic Sources Distribution')

# 4. Engagement vs Impressions
plt.subplot(2, 2, 4)
plt.scatter(df['Impressions'], df['Likes'], alpha=0.5)
plt.xlabel('Impressions')
plt.ylabel('Likes')
plt.title('Impressions vs Likes')

plt.tight_layout()
plt.show()

# Save insights to file
with open('instagram_insights.txt', 'w') as f:
    f.write("=== Instagram Content Performance Insights ===\n\n")
    f.write("1. Overall Channel Performance:\n")
    f.write(f"- Total Posts: {len(df)}\n")
    f.write(f"- Average Impressions: {df['Impressions'].mean():.0f}\n")
    f.write(f"- Average Engagement Rate: {engagement_rate:.2f}%\n")
    f.write(f"- Average Save Rate: {save_rate:.2f}%\n\n")
    
    f.write("2. Content Distribution:\n")
    for source in sources:
        percentage = (traffic[source] / total_traffic) * 100
        f.write(f"- {source}: {percentage:.1f}%\n")
    
    f.write("\n3. Top Performing Content:\n")
    for idx, post in top_posts.iterrows():
        f.write(f"\nPost {idx + 1}:\n")
        f.write(f"Impressions: {post['Impressions']}\n")
        f.write(f"Engagement: {post['Likes'] + post['Comments']}\n")
        f.write(f"Saves: {post['Saves']}\n") 