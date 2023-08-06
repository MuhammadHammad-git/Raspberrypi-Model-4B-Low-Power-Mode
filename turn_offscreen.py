from subprocess import run


def power(onoff):
    run(f'vcgencmd display_power {onoff}', shell=True)
