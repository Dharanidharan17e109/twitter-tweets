tweets=[
    "Early in his career, Tiger was the victim of racial slurs and attacks from a fellow golfer during 1997's Master's Tournament.",
    "This third arrest in the spring of 2007 was for punching a hotel security guard and for yelling homophobic and racial slurs at the arresting officer.",
    "In this instance, he was tape recorded using extremely offensive language, including racial slurs against African-Americans.",
    "His son was dating a black girl and Dog voiced his concern over having her spending time with the family as they have playfully used racial slurs in the past."]
    
"""
  In the above mentioned tweets, i consider the first tweet seems good==>ALLOWED CONTENT SEEMS GOOD!!!,
  Second tweet contains words related to racial slurs but its acceptable,==>ALLOWED,BUT SOMETHING SEEMS WRONG!!!,
  Third tweet must not allowed,==>NOT ALLOWED SOMETHING WRONG WITH CONTENT!!!
  Final tweet contains words related to racial slurs but its acceptable,==>ALLOWED,BUT SOMETHING SEEMS WRONG!!!,
"""

#these are some words related to racial slurs
prohibited_word=["black","African-Americans","offensive","yelling"]
for item in tweets:
    sep=set(item.split(" "))
    prohibited_content_count=0
    prohibited_content_count=set(item).intersection(sep)
    if prohibited_content_count>=2:
        print(item +" ==> "+ "NOT ALLOWED SOMETHING WRONG WITH CONTENT!!!")
    elif prohibited_content_count==1:
        print(item +" ==> "+ "ALLOWED,BUT SOMETHING SEEMS WRONG!!!")
    elif prohibited_content_count>=2:
        print(item +" ==> "+ "ALLOWED CONTENT SEEMS GOOD!!!")