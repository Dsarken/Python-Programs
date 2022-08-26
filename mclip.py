import pyperclip
import sys

# The dictionary with the phrases assigned to the words
TEXT = {
    "agree": "Yes, I agree. That sounds fine to me.",
    "busy": "Sorry, can we do this later this week or next week?",
    "upsell": "Would you consider making this a monthly donation?",
    "meeting": "There will be a meeting soon, I need everyone prepared",
    "disagree": "No, I disagree. Perhaps we could go for an alternative option?"
}
# Checks to see if the length of the
if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for the key phrase has been copied to clipboard: {}".format(keyphrase))
else:
    print("No text for the {}".format(keyphrase))
