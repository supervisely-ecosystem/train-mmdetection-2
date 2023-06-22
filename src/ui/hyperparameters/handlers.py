from typing import List
from supervisely.app.widgets import Widget

from src.ui.hyperparameters.checkpoints import checkpoint_interval_text, checkpoint_interval_input
from src.ui.hyperparameters.general import (
    logfreq_text,
    val_text,
    logfreq_input,
    validation_input,
    epochs_input,
    smaller_size_input,
    bigger_size_input,
)

from src.ui.hyperparameters.optimizers import (
    optimizers_params,
    select_optim,
    apply_clip_input,
    clip_input,
    get_optimizer_params,
)

from src.ui.hyperparameters.lr_scheduler import (
    schedulers_params,
    select_scheduler,
    get_scheduler_params,
)


def show_hide_fields(fields: List[Widget], hide: bool = True):
    for field in fields:
        if hide:
            field.hide()
        else:
            field.show()


@epochs_input.value_changed
def epoch_num_changes(new_value):
    validation_input.max = new_value
    checkpoint_interval_input.max = new_value


@validation_input.value_changed
def update_validation_desc(new_value):
    val_text.text = f"Evaluate validation set every {new_value} epochs"


@logfreq_input.value_changed
def update_logging_desc(new_value):
    logfreq_text.text = f"Log metrics every {new_value} iterations"


@checkpoint_interval_input.value_changed
def update_ch_interval_desc(new_value):
    checkpoint_interval_text.text = f"Save checkpoint every {new_value} epochs"


@apply_clip_input.value_changed
def enable_disable_clip(new_value):
    if new_value:
        clip_input.enable()
    else:
        clip_input.disable()


@select_scheduler.value_changed
def update_scheduler(new_value):
    # print(get_scheduler_params().get_params())
    for scheduler in schedulers_params.keys():
        if new_value == scheduler:
            schedulers_params[scheduler].show()
        else:
            schedulers_params[scheduler].hide()


@select_optim.value_changed
def update_optim(new_value):
    print(get_optimizer_params().get_params())
    for optim in optimizers_params.keys():
        if new_value == optim:
            optimizers_params[optim].show()
        else:
            optimizers_params[optim].hide()


@smaller_size_input.value_changed
def set_min_for_max_size(new_min):
    bigger_size_input.min = new_min


@bigger_size_input.value_changed
def set_max_for_min_size(new_max):
    smaller_size_input.max = new_max
