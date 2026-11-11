
from drafter import *
from dataclasses import dataclass


# Represents one car in the project car database.
@dataclass
class Car:
    make: str
    model: str
    year: int
    region: str
    transmission: str


# Stores the user's selections and the car database.
@dataclass
class State:
    cars: list[Car]
    regions: list[str]
    year_min: int
    year_max: int
    transmission: str
    make: str
    model: str


def create_cars() -> list[Car]:
    """Create and return the sample database of pre-2000 project cars."""
    return [
        Car("Ford", "Mustang", 1965, "American", "Manual"),
        Car("Chevrolet", "Camaro", 1969, "American", "Manual"),
        Car("Dodge", "Charger", 1968, "American", "Automatic"),
        Car("Pontiac", "Firebird", 1977, "American", "Manual"),
        Car("Chevrolet", "Corvette", 1990, "American", "Manual"),

        Car("Nissan", "Skyline GT-R", 1995, "JDM", "Manual"),
        Car("Toyota", "Supra", 1994, "JDM", "Manual"),
        Car("Mazda", "RX-7", 1993, "JDM", "Manual"),
        Car("Honda", "NSX", 1991, "JDM", "Manual"),
        Car("Mitsubishi", "3000GT", 1991, "JDM", "Manual"),
        Car("Subaru", "Impreza WRX", 1998, "JDM", "Manual"),

        Car("Hyundai", "Scoupe", 1995, "KDM", "Manual"),
        Car("Kia", "Sephia", 1996, "KDM", "Automatic"),

        Car("BMW", "M3", 1995, "German", "Manual"),
        Car("Porsche", "911", 1997, "German", "Manual"),
        Car("Mercedes-Benz", "190E", 1991, "German", "Automatic"),
        Car("Volkswagen", "Golf GTI", 1998, "German", "Manual"),
        Car("Audi", "S4", 1992, "German", "Manual"),

        Car("Volvo", "850", 1995, "European", "Automatic"),
        Car("Peugeot", "205 GTI", 1988, "European", "Manual"),
        Car("Alfa Romeo", "Spider", 1990, "European", "Manual"),
        Car("Lotus", "Elise", 1996, "European", "Manual"),
                # Additional American project cars
        Car("Ford", "Mustang Foxbody", 1987, "American", "Manual"),
        Car("Chevrolet", "Chevelle SS", 1970, "American", "Manual"),
        Car("Chevrolet", "Nova", 1972, "American", "Automatic"),
        Car("Dodge", "Challenger", 1970, "American", "Manual"),
        Car("Pontiac", "GTO", 1967, "American", "Manual"),
        Car("Buick", "Grand National", 1987, "American", "Automatic"),
        Car("Chevrolet", "Impala", 1964, "American", "Automatic"),

        # Additional Japanese (JDM) project cars
        Car("Nissan", "240SX", 1995, "JDM", "Manual"),
        Car("Nissan", "300ZX", 1992, "JDM", "Manual"),
        Car("Nissan", "Silvia S14", 1996, "JDM", "Manual"),
        Car("Toyota", "AE86 Corolla", 1985, "JDM", "Manual"),
        Car("Toyota", "MR2", 1991, "JDM", "Manual"),
        Car("Toyota", "Celica GT-Four", 1994, "JDM", "Manual"),
        Car("Mazda", "Miata MX-5", 1994, "JDM", "Manual"),
        Car("Mazda", "RX-3", 1975, "JDM", "Manual"),
        Car("Honda", "Civic EG", 1993, "JDM", "Manual"),
        Car("Honda", "Integra Type R", 1997, "JDM", "Manual"),
        Car("Mitsubishi", "Lancer Evolution V", 1998, "JDM", "Manual"),
        Car("Subaru", "Legacy GT", 1996, "JDM", "Manual"),

        # Additional Korean (KDM) project cars
        Car("Hyundai", "Tiburon", 1998, "KDM", "Manual"),
        Car("Hyundai", "Excel", 1994, "KDM", "Manual"),
        Car("Daewoo", "Lanos", 1999, "KDM", "Manual"),

        # Additional German project cars
        Car("BMW", "E30 325i", 1989, "German", "Manual"),
        Car("BMW", "E36 328i", 1997, "German", "Manual"),
        Car("BMW", "E46 330i", 1999, "German", "Manual"),
        Car("Porsche", "944", 1986, "German", "Manual"),
        Car("Porsche", "928", 1987, "German", "Automatic"),
        Car("Volkswagen", "Corrado VR6", 1995, "German", "Manual"),
        Car("Audi", "Quattro", 1985, "German", "Manual"),

        # Additional European project cars
        Car("Lotus", "Esprit", 1993, "European", "Manual"),
        Car("Jaguar", "XJ-S", 1989, "European", "Automatic"),
        Car("Peugeot", "306 GTI", 1998, "European", "Manual"),
        Car("Renault", "Clio Williams", 1996, "European", "Manual"),
        Car("Fiat", "X1/9", 1978, "European", "Manual"),
        Car("Alfa Romeo", "GTV", 1998, "European", "Manual")
    ]


@route
def index(state: State) -> Page:
    """Display the homepage and introduce the Project Car Finder."""
    return Page(state, [
        Header("Project Car Finder"),
        "Find your next classic project car!",
        "This website helps you narrow down pre-2000 cars "
        "based on their origin, year, transmission, and manufacturer.",
        "",
        Header("How it works"),
        "You will answer five filter questions before receiving "
        "a list of cars matching your preferences.",
        "",
        Button("Start Finding Cars", "region_page")
    ])


@route
def region_page(state: State) -> Page:
    """Display checkboxes allowing users to select multiple regions."""
    return Page(state, [
        Header("Step 1: Choose a Region"),
        "Where would you like your project car to originate?",
        "You can select multiple regions.",
        "",
        RelatedCheckBox("regions", "American"),
        " American",
        RelatedCheckBox("regions", "JDM"),
        " Japanese Domestic Market (JDM)",
        RelatedCheckBox("regions", "KDM"),
        " Korean Domestic Market (KDM)",
        RelatedCheckBox("regions", "German"),
        " German",
        RelatedCheckBox("regions", "European"),
        " Other European",
        "",
        Button("Next: Choose a Year", "year_page")
    ])


@route
def year_page(state: State, regions: list[str]) -> Page:
    """Save selected regions and ask the user for a year range."""
    state.regions = regions

    return Page(state, [
        Header("Step 2: Choose a Year Range"),
        "What year range are you interested in?",
        "Only cars manufactured before 2000 are included.",
        "",
        "Earliest year:",
        TextBox("year_min", state.year_min),
        "",
        "Latest year:",
        TextBox("year_max", state.year_max),
        "",
        Button("Next: Choose Transmission", "transmission_page")
    ])


@route
def transmission_page(state: State,
                      year_min: int,
                      year_max: int) -> Page:
    """Save the year range and display transmission preferences."""
    state.year_min = max(1900, year_min)
    state.year_max = min(1999, year_max)

    if state.year_min > state.year_max:
        state.year_min, state.year_max = (
            state.year_max, state.year_min
        )

    return Page(state, [
        Header("Step 3: Choose a Transmission"),
        "Which transmission style do you prefer?",
        "",
        SelectBox(
            "transmission",
            ["Any", "Manual", "Automatic"],
            state.transmission
        ),
        "",
        Button("Next: Choose a Make", "make_page")
    ])


@route
def make_page(state: State, transmission: str) -> Page:
    """Save the transmission preference and ask for a manufacturer."""
    state.transmission = transmission

    return Page(state, [
        Header("Step 4: Choose a Manufacturer"),
        "Do you have a preferred car manufacturer?",
        "Examples: Toyota, Ford, BMW, Nissan, Honda.",
        "Leave the textbox blank if you have no preference.",
        "",
        TextBox("make", state.make),
        "",
        Button("Next: Choose a Model", "model_page")
    ])


@route
def model_page(state: State, make: str) -> Page:
    """Save the manufacturer and ask for a specific car model."""
    state.make = make

    return Page(state, [
        Header("Step 5: Choose a Model"),
        "Are you looking for a particular model?",
        "Examples: Supra, Mustang, Skyline GT-R, RX-7.",
        "Leave the textbox blank if you have no preference.",
        "",
        TextBox("model", state.model),
        "",
        Button("Find My Project Car!", "results")
    ])


@route
def results(state: State, model: str) -> Page:
    """Filter the car database and display all matching cars."""
    state.model = model

    matching_cars = []

    for car in state.cars:
        region_matches = (
            len(state.regions) == 0
            or car.region in state.regions
        )

        year_matches = (
            state.year_min <= car.year <= state.year_max
        )

        transmission_matches = (
            state.transmission == "Any"
            or car.transmission == state.transmission
        )

        make_matches = (
            state.make.strip() == ""
            or state.make.lower() in car.make.lower()
        )

        model_matches = (
            state.model.strip() == ""
            or state.model.lower() in car.model.lower()
        )

        if (region_matches and year_matches
                and transmission_matches
                and make_matches and model_matches):
            matching_cars.append(car)

    car_results = []

    for car in matching_cars:
        car_results.append(
            car.make + " " + car.model
            + " | Year: " + str(car.year)
            + " | Region: " + car.region
            + " | Transmission: " + car.transmission
        )

    if len(matching_cars) == 0:
        return Page(state, [
            Header("No Matching Cars Found"),
            "Unfortunately, no cars matched your filters.",
            "Try changing your preferences.",
            "",
            Button("Start Over", "index")
        ])

    return Page(state, [
        Header("Your Project Car Results!"),
        "We found " + str(len(matching_cars)) + " matching cars!",
        "",
        BulletedList(car_results),
        "",
        Button("Start Over", "index"),
        Button("Change Preferences", "region_page")
    ])


# Start the website with its initial state.
start_server(State(
    cars=create_cars(),
    regions=[],
    year_min=1900,
    year_max=1999,
    transmission="Any",
    make="",
    model=""
))


