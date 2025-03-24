import click
from bullet import Bullet
from rifle import Rifle
from environment import Environment
from target import Target

# Global config to store instances
config = {"bullet": None, "rifle": None, "environment": None, "target": None}

# Create a Click group
@click.group()
def cli():
    """Ballistic Calculator Setup"""
    pass

# Subcommand for Bullet setup
@cli.command()
@click.option('--name', prompt='Name of the Bullet', type=str, help='Name of the Bullet')
@click.option('--weight', prompt='Bullet weight (grains)', type=float, help='Bullet weight in grains')
@click.option('--diameter', prompt='Bullet diameter (inches)', type=float, help='Bullet diameter in inches')
@click.option('--bc', prompt='Ballistic coefficient', type=float, help='Ballistic coefficient')
@click.option('--drag-function', prompt='Drag function (e.g., G1, G7)', help='Drag function type')
def setup_bullet(name, weight, diameter, bc, drag_function):
    """Set up bullet parameters"""
    bullet = Bullet(name,weight, diameter, bc, drag_function)
    config["bullet"] = bullet
    click.echo(f"Bullet configured: {bullet}")

# Subcommand for Rifle setup
@cli.command()
@click.option('--name', prompt='Name of the Rifle', type=str, help='Name of the Rifle')
@click.option('--muzzle-velocity', prompt='Muzzle velocity (fps)', type=float, help='Muzzle velocity in fps')
@click.option('--barrel-twist', prompt='Barrel twist (e.g., 10 for 1:10)', type=float, help='Barrel twist rate')
@click.option('--sight-height', prompt='Sight height (inches)', type=float, help='Sight height in inches')
@click.option('--zero-range', prompt='Zero range (yards)', type=float, help='Zero range in yards')
def setup_rifle(name, muzzle_velocity, barrel_twist, sight_height, zero_range):
    """Set up rifle parameters"""
    rifle = Rifle(name, muzzle_velocity, barrel_twist, sight_height, zero_range)
    config["rifle"] = rifle
    click.echo(f"Rifle configured: {rifle}")

# Subcommand for Environment setup
@cli.command()
@click.option('--wind-speed', prompt='Wind speed (mph)', type=float, help='Wind speed in mph')
@click.option('--wind-direction', prompt='Wind direction (degrees)', type=float, help='Wind direction in degrees')
@click.option('--temperature', prompt='Temperature (F)', type=float, help='Temperature in Fahrenheit')
@click.option('--humidity', prompt='Humidity (%)', type=float, help='Humidity percentage')
@click.option('--pressure', prompt='Pressure (inHg)', type=float, help='Pressure in inches Hg')
@click.option('--altitude', prompt='Altitude (feet)', type=float, help='Altitude in feet')
def setup_environment(wind_speed, wind_direction, temperature, humidity, pressure, altitude):
    """Set up environment parameters"""
    env = Environment(wind_speed, wind_direction, temperature, humidity, pressure, altitude)
    config["environment"] = env
    click.echo(f"Environment configured: {env}")

# Subcommand for Target setup
@cli.command()
@click.option('--distance', prompt='Target distance (yards)', type=float, help='Distance to target in yards')
@click.option('--angle', prompt='Target angle (degrees)', type=float, help='Angle to target in degrees')
def setup_target(distance, angle):
    """Set up target parameters"""
    target = Target(distance, angle)
    config["target"] = target
    click.echo(f"Target configured: {target}")

# Optional: Add a command to show current config
@cli.command()
def show_config():
    """Show current configuration"""
    for key, value in config.items():
        click.echo(f"{key.capitalize()}: {value if value else 'Not set'}")

if __name__ == '__main__':
    cli()