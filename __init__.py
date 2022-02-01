from modloader.modclass import Mod, loadable_mod
import modloader.modinfo as modinfo

def adine_endings(ml):
    ( ml.find_label('_call_endingjustafewminuteslater_4')
        .search_python('renpy.block_rollback()', depth=600)
        .hook_to('skipcredits_four_adine5bad_credits_start')
        .search_scene('logo')
        .search_python('renpy.pause (10.0)')
        .hook_to('skipcredits_four_adine5bad_credits_done')
    )

    ( ml.find_label('adinegoodending')
        .search_python('renpy.block_rollback()', depth=400)
        .hook_to('skipcredits_four_adine5good_credits_start')
        .search_scene('logo')
        .search_python('renpy.pause (10.0)')
        .hook_to('skipcredits_four_adine5good_credits_done')
    )


def anna_endings(ml):
    ( ml.find_label('_call_endingjustafewminuteslater_1')
        .search_python('renpy.block_rollback()', depth=600)
        .hook_to('skipcredits_four_anna5bad_credits_start')
        .search_scene('logo')
        .search_python('renpy.pause (10.0)')
        .hook_to('skipcredits_four_anna5bad_credits_done')
    )

    ( ml.find_label('annagoodending')
        .search_python('_game_menu_screen = None', depth=400)
        .hook_to('skipcredits_four_anna5good_credits_start')
        .search_scene('logo')
        .search_python('renpy.pause (7.0)')
        .hook_to('skipcredits_four_anna5good_credits_done')
    )


def bryce_endings(ml):
    ( ml.find_label('_call_sincethelightswerealreadyon')
        .search_python('renpy.block_rollback()', depth=600)
        .hook_to('skipcredits_four_bryce5bad_credits_start')
        .search_scene('logo')
        .search_python('renpy.pause (10.0)')
        .hook_to('skipcredits_four_bryce5bad_credits_done')
    )

    ( ml.find_label('brycegoodending')
        .search_python('renpy.block_rollback()', depth=800)
        .hook_to('skipcredits_four_bryce5good_credits_start')
        .search_scene('logo')
        .search_python('renpy.pause (8.5)')
        .hook_to('skipcredits_four_bryce5good_credits_done')
    )


def lorem_endings(ml):
    ( ml.find_label('loremgoodending2')
        .search_python('renpy.block_rollback()', depth=600)
        .hook_to('skipcredits_four_lorem5bad_credits_start')
        .search_scene('logo')
        .search_python('renpy.pause (5.0)')
        .hook_to('skipcredits_four_lorem5bad_credits_done')
    )

    ( ml.find_label('loremgoodending3')
        .search_python('renpy.block_rollback()', depth=400)
        .hook_to('skipcredits_four_lorem5good_credits_start')
        .search_scene('logo')
        .search_python('renpy.pause (1.0)')
        .hook_to('skipcredits_four_lorem5good_credits_done')
    )


def neutral_ending(ml):
    ( ml.find_label('_call_endingjustafewminuteslater')
        .search_python('renpy.block_rollback()', depth=600)
        .hook_to('skipcredits_four_neutral_credits_start')
        .search_scene('logo')
        .search_python('renpy.pause (10.0)')
        .hook_to('skipcredits_four_neutral_credits_done')
    )


def remy_endings(ml):
    ( ml.find_label('_call_endingjustafewminuteslater_2')
        .search_python('renpy.block_rollback()', depth=700)
        .hook_to('skipcredits_four_remy5bad_credits_start')
        .search_scene('logo')
        .search_python('renpy.pause (9.0)')
        .hook_to('skipcredits_four_remy5bad_credits_done')
    )

    ( ml.find_label('remygoodending')
        .search_python('renpy.block_rollback()', depth=400)
        .hook_to('skipcredits_four_remy5good_credits_start')
        .search_scene('logo')
        .search_python('renpy.pause (8.5)')
        .hook_to('skipcredits_four_remy5good_credits_done')
    )


def true_ending(ml):
    ( ml.find_label('trueendings')
        .search_python('renpy.block_rollback()', depth=2100)
        .hook_to('skipcredits_four_trueending_credits_start')
        .search_show('creditsx2', depth=300)
        .search_python('renpy.pause (5.0)')
        .hook_to('skipcredits_four_trueending_credits_done')
    )


@loadable_mod
class MyAwSWMod(Mod):
    name = "Skip Credits"
    version = "v1.0"
    author = "4onen"
    dependencies = ["MagmaLink"]

    @staticmethod
    def mod_load():
        ml = modinfo.get_mods()["MagmaLink"].import_ml()
        adine_endings(ml)
        anna_endings(ml)
        bryce_endings(ml)
        lorem_endings(ml)
        neutral_ending(ml)
        remy_endings(ml)
        true_ending(ml)

    @staticmethod
    def mod_complete():
        pass
