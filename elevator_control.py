from elevator_management.system_manager_singleton import SystemManagerSingleton


class ElevatorControl:
    def __init__(self, identifier):
        self.__hw_link = None
        self.__identifier = identifier
        self.initialize_elevator()
        self.__current_destination_floor = self.current_floor
        SystemManagerSingleton.get_instance().register_elevator_controller(controller_instance=self)

    @property
    def current_speed(self):
        return self.__hw_link.get_speed()

    @property
    def direction(self):
        return self.__hw_link.get_direction()

    @property
    def identifier(self):
        return self.__identifier

    @property
    def current_floor(self):
        return self.__hw_link.get_location()

    def initialize_elevator(self):
        """
        This is where there would be some stuff to setup a link to the elevators hardware
        :return:
        """
        # self.__hw_link = something to setup a hardware link to the elevator itself.
        pass

    def go_to_floor(self, floor):
        """
        Set the given floor as current destination, and move elevator towards it.
        :param floor: The floor to go to
        """
        self.validate_floor(floor)
        self.can_stop_at_floor(floor)
        self.__current_destination_floor = floor
        # do what must be done to get the elevator moving toward the given floor, and ensure it slows down and stops at
        # the given floor

    def has_arrived(self):
        """
        Triggered by elevator hardware event.
        Notifies queue so new destination can be given
        :return:
        """
        SystemManagerSingleton.get_instance().remove_destination(identifier=self.identifier,
                                                                 destination_floor=self.__current_destination_floor)

    def validate_floor(self, floor):
        """
        check that floor is valid, raise error if it does not exist.
        """
        if not self.__hw_link.has_floor(floor=floor):
            raise ValueError(f'Floor {floor} does not exist for elevator {self.identifier}')

    def can_stop_at_floor(self, floor):
        """
        check current speed and direction and see if we can actually stop at given floor now.
        Raise error if not.
        """
        pass

    def emergency_stop(self):
        """
        stop elevator immediately and sound alarm
        """
        self.__hw_link.stop(force=True)
        self.__hw_link.enable_alarm()
