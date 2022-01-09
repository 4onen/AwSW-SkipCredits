screen skipcredits_four_screen(towhere):
    textbutton "Skip >>":
        action [Play("audio", "se/sounds/select3.ogg"), Hide('skipcredits_four_screen'), Jump(towhere)]
        hovered Play("audio", "se/sounds/select.ogg")
        xanchor 0.5
        yanchor 1.0
        xalign 0.5
        yalign 0.95

        style "menubutton"


# Adine endings

label skipcredits_four_adine5bad_credits_start:
    show screen skipcredits_four_screen('skipcredits_four_adine5bad_credits_done')
    jump skipcredits_four_adine5bad_credits_start_return

label skipcredits_four_adine5bad_credits_done:
    hide screen skipcredits_four_screen
    jump skipcredits_four_adine5bad_credits_done_return

label skipcredits_four_adine5good_credits_start:
    show screen skipcredits_four_screen('skipcredits_four_adine5good_credits_done')
    jump skipcredits_four_adine5good_credits_start_return

label skipcredits_four_adine5good_credits_done:
    hide screen skipcredits_four_screen
    jump skipcredits_four_adine5good_credits_done_return


# Anna endings

label skipcredits_four_anna5bad_credits_start:
    show screen skipcredits_four_screen('skipcredits_four_anna5bad_credits_done')
    jump skipcredits_four_anna5bad_credits_start_return

label skipcredits_four_anna5bad_credits_done:
    hide screen skipcredits_four_screen
    jump skipcredits_four_anna5bad_credits_done_return

label skipcredits_four_anna5good_credits_start:
    show screen skipcredits_four_screen('skipcredits_four_anna5good_credits_done')
    jump skipcredits_four_anna5good_credits_start_return

label skipcredits_four_anna5good_credits_done:
    hide screen skipcredits_four_screen
    jump skipcredits_four_anna5good_credits_done_return



# Bryce endings

label skipcredits_four_bryce5bad_credits_start:
    show screen skipcredits_four_screen('skipcredits_four_bryce5bad_credits_done')
    jump skipcredits_four_bryce5bad_credits_start_return

label skipcredits_four_bryce5bad_credits_done:
    hide screen skipcredits_four_screen
    jump skipcredits_four_bryce5bad_credits_done_return

label skipcredits_four_bryce5good_credits_start:
    show screen skipcredits_four_screen('skipcredits_four_bryce5good_credits_done')
    jump skipcredits_four_bryce5good_credits_start_return

label skipcredits_four_bryce5good_credits_done:
    hide screen skipcredits_four_screen
    jump skipcredits_four_bryce5good_credits_done_return


# Lorem's endings

label skipcredits_four_lorem5bad_credits_start:
    show screen skipcredits_four_screen('skipcredits_four_lorem5bad_credits_done')
    jump skipcredits_four_lorem5bad_credits_start_return

label skipcredits_four_lorem5bad_credits_done:
    hide screen skipcredits_four_screen
    jump skipcredits_four_lorem5bad_credits_done_return

label skipcredits_four_lorem5good_credits_start:
    show screen skipcredits_four_screen('skipcredits_four_lorem5good_credits_done')
    jump skipcredits_four_lorem5good_credits_start_return

label skipcredits_four_lorem5good_credits_done:
    hide screen skipcredits_four_screen
    jump skipcredits_four_lorem5good_credits_done_return


# Neutral ending

label skipcredits_four_neutral_credits_start:
    show screen skipcredits_four_screen('skipcredits_four_neutral_credits_done')
    jump skipcredits_four_neutral_credits_start_return

label skipcredits_four_neutral_credits_done:
    hide screen skipcredits_four_screen
    jump skipcredits_four_neutral_credits_done_return


# Remy's endings

label skipcredits_four_remy5bad_credits_start:
    show screen skipcredits_four_screen('skipcredits_four_remy5bad_credits_done')
    jump skipcredits_four_remy5bad_credits_start_return

label skipcredits_four_remy5bad_credits_done:
    hide screen skipcredits_four_screen
    jump skipcredits_four_remy5bad_credits_done_return

label skipcredits_four_remy5good_credits_start:
    show screen skipcredits_four_screen('skipcredits_four_remy5good_credits_done')
    jump skipcredits_four_remy5good_credits_start_return

label skipcredits_four_remy5good_credits_done:
    hide screen skipcredits_four_screen
    jump skipcredits_four_remy5good_credits_done_return


# True ending

label skipcredits_four_trueending_credits_start:
    show screen skipcredits_four_screen('skipcredits_four_trueending_credits_done')
    jump skipcredits_four_trueending_credits_start_return

label skipcredits_four_trueending_credits_done:
    hide screen skipcredits_four_screen
    window hide
    nvl clear
    jump skipcredits_four_trueending_credits_done_return