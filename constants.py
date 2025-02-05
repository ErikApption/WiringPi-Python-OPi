%pythoncode %{
# wiringopi modes

WPI_MODE_PINS = 0;
WPI_MODE_GPIO = 1;
WPI_MODE_GPIO_SYS = 2;
WPI_MODE_PHYS = 3;
WPI_MODE_PIFACE = 4;
WPI_MODE_UNINITIALISED = -1;

# Pin modes

INPUT = 0;
OUTPUT = 1;
PWM_OUTPUT = 2;
GPIO_CLOCK = 3;
SOFT_PWM_OUTPUT = 4;
SOFT_TONE_OUTPUT = 5;
PWM_TONE_OUTPUT = 6;

LOW = 0;
HIGH = 1;

# Pull up/down/none

PUD_OFF = 0;
PUD_DOWN = 1;
PUD_UP = 2;

# PWM

PWM_MODE_MS = 0;
PWM_MODE_BAL = 1;

# Interrupt levels

INT_EDGE_SETUP = 0;
INT_EDGE_FALLING = 1;
INT_EDGE_RISING = 2;
INT_EDGE_BOTH = 3;

# Shifting (from wiringShift.h)

LSBFIRST = 0;
MSBFIRST = 1;

%}
