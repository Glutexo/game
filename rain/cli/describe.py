def describe_history(index, state):
    description = describe_state(state)
    return f"{index} {description}"


def describe_state(state):
    return f"The active player is {state.active_player}"
