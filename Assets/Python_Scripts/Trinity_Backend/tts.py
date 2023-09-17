import elevenlabs
import json 
elevenlabs.set_api_key("76e3f03269d40cae06ca57975669fd3b")

def tts(text):
    text = text.split('\n')
    speaker1 = True
    for i in range(len(text)):
        line = text[i]
        
        if len(line) < 2:
            continue
        parts = line.split(':')
        name = parts[0]
        message = parts[1]

        if speaker1:
            voice = elevenlabs.Voice(
                voice_id = "ZQe5CZNOzWyzPSCn5a3c",
                settings = elevenlabs.VoiceSettings(
                    stability = 0.7,
                    similarity_boost = 0.75
                )
            )
            audio = elevenlabs.generate(
                text = message,
                voice = "Patrick"
            )
            speaker1 = False
        else:
            voice = elevenlabs.Voice(
                voice_id = "ZQe5CZNOzWyzPSCn5a3c",
                settings = elevenlabs.VoiceSettings(
                    stability = 0.7,
                    similarity_boost = 0.75
                )
            )
            audio = elevenlabs.generate(
                text = message,
                voice = "Matthew"
            )
            speaker1 = True
        elevenlabs.play(audio)
    
    # for name, message in text.items():
    #     print(name)
    #     print(message)
    #     if name == "Gabe":
    #         voice = elevenlabs.Voice(
    #             voice_id = "ZQe5CZNOzWyzPSCn5a3c",
    #             settings = elevenlabs.VoiceSettings(
    #                 stability = 0.7,
    #                 similarity_boost = 0.75
    #             )
    #         )

    #         audio = elevenlabs.generate(
    #             text = message,
    #             voice = "Patrick"
    #         )
    #         elevenlabs.play(audio)
    #     if name == "Dinesh":
    #         voice = elevenlabs.Voice(
    #             voice_id = "ZQe5CZNOzWyzPSCn5a3c",
    #             settings = elevenlabs.VoiceSettings(
    #                 stability = 0.7,
    #                 similarity_boost = 0.75
    #             )
    #         )

    #         audio = elevenlabs.generate(
    #             text = message,
    #             voice = "Matthew"
    #         )
    #         elevenlabs.play(audio)
    # elevenlabs.save(audio, "audio.mp3")

# text='''"Gabe": "Wow, that's/ incredible news, Dinesh.",
#   "Dinesh": "Absolutely, Gabe.",
#   "Gabe": "Oh, a coding competition? You know I'm in! I'd love to test my skills against yours. But let's make a pact, no matter who wins, we'll always prioritize our project and continue supporting each other.",
#   "Dinesh": "Deal! We're a team first, Gabe. We'll keep our competitive spirits in check and focus on what truly matters. Together, we can achieve pure brilliance in our work."
#   '''

# # text = json.loads(text)
# # print(type(text))
# text = text.split('\n')
# tts(text)

