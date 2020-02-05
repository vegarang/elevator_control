from elevator_management.system_manager_singleton import SystemManagerSingleton


class ButtonControl:
    """
    Controller-class for a single button.
    """
    def __init__(self, identifier, elevator_identifier_list, hardware_channel, floor):
        """
        store instance-values, initialize button-listener, and register self as a buttoncontroller in SystemManager.

        :param elevator_identifier_list: list of elevator identifiers for the elevators this should be registered for
        :param identifier: internal identifier for this button
        :param hardware_channel: channel to listen for button-input on
        :param floor: the floor this button should send the elevator to
        """
        self.__hw_link = None
        self.__elevator_identifier_list = elevator_identifier_list
        self.__identifier = identifier
        self.__hardware_channel = hardware_channel
        self.__floor = floor
        self.initialize_hw_button()
        SystemManagerSingleton.get_instance().register_button_controller(controller_instance=self)

    @property
    def identifier(self):
        return self.__identifier

    @property
    def elevator_identifier_list(self):
        return self.__elevator_identifier_list

    @property
    def floor(self):
        return self.__floor

    @property
    def hardware_channel(self):
        return self.__hardware_channel

    def initialize_hw_button(self):
        """
        This is where there should be some stuff to listen for a button-input.
        A button-input should trigger ``button_clicked``
        :return:
        """
        # self.__hw_link = something to initalize button
        pass

    def set_button_light(self, on=True):
        """
        turn button light on or off depending on given param.
        """
        if on:
            self.__hw_link.enable_light()
        else:
            self.__hw_link.disable_light()

    def button_clicked(self):
        """
        Button was clicked!
        If not already in queue, add click to queue, and trigger light
        :return:
        """
        SystemManagerSingleton.get_instance().add_destination(button_identifier=self.identifier)