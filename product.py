from design_modules.component import BasicComponent

class Monsoon:
    def __init__(
            self,
            frame:BasicComponent,
            wheel:BasicComponent,
            mechanism:BasicComponent,
            saddle:BasicComponent,
            box:BasicComponent,
            motor:BasicComponent,
            battery:BasicComponent,
        ):
        self.number_per_pallet = 5
        self.average_industrial_usage = 1000
        self.basic_price = 2000
        
        self.components = [
            frame,
            wheel,
            wheel,
            mechanism,
            saddle,
            box,
            motor,
            battery
        ]