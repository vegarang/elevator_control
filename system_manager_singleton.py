class SystemManagerSingleton:
    """
    Singleton to manage elevators.

    Ensures elevators move where they are supposed to in a sane order.
    """
    __instance = None

    @staticmethod
    def get_instance():
        if SystemManagerSingleton.__instance == None:
            SystemManagerSingleton()
        return SystemManagerSingleton.__instance

    def __init__(self):
        if SystemManagerSingleton.__instance != None:
            raise Exception("This class is a singleton!")

        SystemManagerSingleton.__instance = self

        #: dictionary of controllers for different elevators.
        self.elevator_controllers = {}

        #: dictionary of controllers for different elevator-buttons.
        self.button_controllers = {}

        #: dictionary of queues for different elevators.
        self.elevator_queues = {}

    def register_elevator_controller(self, controller_instance):
        """
        Register an elevator controller and initialize a queue for it
        :param identifier: identity for the controller
        :param controller_instance: the :class:`ElevatorControl`-instance for a given elevator
        """
        self.elevator_controllers[controller_instance.identifier] = controller_instance

    def register_button_controller(self, controller_instance):
        """
        register a button controller.
        :param controller_instance: the :class:`ButtonController`-instance for a given elevator-button
        """
        self.button_controllers[controller_instance.identifier] = controller_instance

    def initialize_queue(self, identifier):
        """
        setup queues for all available elevators
        :return:
        """
        # something like:
        # Note: queue itself is not implemented..
        # self.elevator_queues[identifier] = ThreadSafeQueue()
        pass

    def remove_destination(self, identifier, destination_floor):
        """
        Remove given destination from queue for given elevator. If queue for given elevator is not empty, calculate
        next destination for elevator

        :param identifier: identifier for elevator
        :param destination_floor: the floor the elevator just reached.
        """
        self.elevator_queues[identifier].remove_destination(destination=destination_floor)

        new_destination = self.calculate_destination(identifier)
        self.elevator_controllers[identifier].go_to_destination(new_destination)
        self.turn_off_lights_for_buttons_for_floor(elevator_identifier=identifier, floor=destination_floor)

    def add_destination(self, button_identifier):
        """
        Add a destination to the queue for an elevator.
        Turn on light for button.

        :param button_identifier:
        """
        button_controller = self.button_controllers[button_identifier]
        for elevator_identifier in button_controller.elevator_identifier_list:
            self.elevator_queues[elevator_identifier].add_destination(destination=button_controller.floor)
        button_controller.set_light(on=True)

    def calculate_destination(self, identifier):
        """
        Calculate new destination from queue for given identifier
        :param identifier:
        :return: destination floor, or first floor if queue is empty
        """
        if self.elevator_queues[identifier].is_empty():
            return 1
        # do something to calculate next floor based on current floor, current direction, time since button-press etc..
        # if the calculated floor is in the queue for multiple elevators, remove it from others.

    def calculate_time_to_destination(self, elevator_identifier, floor):
        """
        Calculate how much time it will take for a given elevator to get to a given floor.
        :param elevator_identifier: the identifier of the elevator
        :param floor: floor number
        :return:
        """
        # see what number the floor is in queue (if present), see if it's along the path to one who's earlier in the
        # queue, and calculate approximate travel time
        pass

    def turn_off_lights_for_buttons_for_floor(self, elevator_identifier, floor):
        """
        find all buttons for a given elevator for a given floor and turn the light off.
        """
        pass
