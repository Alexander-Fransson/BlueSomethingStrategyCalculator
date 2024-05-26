class RSP:
    def __init__(
        self,
        rsp_transport_cost_per_product:float,
        dissasembly_capacity_products_per_day:int,
        remanufacturing_capacity_components_per_day:int,
        recycling_capacity_kg_per_day:int,
        dissasembly_loss:float,
        component_remanufacturing_efficiency:float,
        material_recycling_efficiency:float,
        dissasembly_cost_per_piece:float,
        energy_cost_of_recycling_a_ton:float,
        remanufacture:bool,
        recycle:bool
    ):
        self.rsp_transport_cost = rsp_transport_cost_per_product
        self.dissasembly_capacity = dissasembly_capacity_products_per_day
        self.remanufacturing_capacity = remanufacturing_capacity_components_per_day
        self.recycling_capacity = recycling_capacity_kg_per_day
        self.dissasembly_loss = dissasembly_loss
        self.component_remanufacturing_efficiency = component_remanufacturing_efficiency
        self.material_recycling_efficiency = material_recycling_efficiency
        self.dissasembly_cost = dissasembly_cost_per_piece
        self.energy_cost_of_recycling_a_ton = energy_cost_of_recycling_a_ton
        self.remanufacture = remanufacture
        self.recycle = recycle

class RSPs:
    def __init__(self):

        # We might be able to negotiate with these for better circularity better circularity

        self.GreenCycle = RSP(
            rsp_transport_cost_per_product=12.00,
            dissasembly_capacity_products_per_day=150,
            remanufacturing_capacity_components_per_day=200,
            recycling_capacity_kg_per_day=1000,
            dissasembly_loss=.06,
            component_remanufacturing_efficiency=.4,
            material_recycling_efficiency=.95,
            dissasembly_cost_per_piece=32.00,
            energy_cost_of_recycling_a_ton=50.00
        )
        self.New_Life =  RSP(
            rsp_transport_cost_per_product=22.00,
            dissasembly_capacity_products_per_day=100,
            remanufacturing_capacity_components_per_day=500,
            recycling_capacity_kg_per_day=1000,
            dissasembly_loss=.04,
            component_remanufacturing_efficiency=.88,
            material_recycling_efficiency=.5,
            dissasembly_cost_per_piece=88.00,
            energy_cost_of_recycling_a_ton=90.00
        )
        self.Repairly = RSP(
            rsp_transport_cost_per_product=25.00,
            dissasembly_capacity_products_per_day=300,
            remanufacturing_capacity_components_per_day=1000,
            recycling_capacity_kg_per_day=1000,
            dissasembly_loss=.05,
            component_remanufacturing_efficiency=.85,
            material_recycling_efficiency=.5,
            dissasembly_cost_per_piece=96.00,
            energy_cost_of_recycling_a_ton=100.00
        )
        self.Thrashless = RSP(
            rsp_transport_cost_per_product=20.00,
            dissasembly_capacity_products_per_day=75,
            remanufacturing_capacity_components_per_day=300,
            recycling_capacity_kg_per_day=1000,
            dissasembly_loss=.11,
            component_remanufacturing_efficiency=.55,
            material_recycling_efficiency=.6,
            dissasembly_cost_per_piece=80.00,
            energy_cost_of_recycling_a_ton=100.00
        )
        self.Revalue = RSP(
            rsp_transport_cost_per_product=14.00,
            dissasembly_capacity_products_per_day=75,
            remanufacturing_capacity_components_per_day=400,
            recycling_capacity_kg_per_day=1000,
            dissasembly_loss=.12,
            component_remanufacturing_efficiency=.75,
            material_recycling_efficiency=.7,
            dissasembly_cost_per_piece=64.00,
            energy_cost_of_recycling_a_ton=100.00
        )
        self.NewKid = RSP(
            rsp_transport_cost_per_product=17.00,
            dissasembly_capacity_products_per_day=50,
            remanufacturing_capacity_components_per_day=200,
            recycling_capacity_kg_per_day=1000,
            dissasembly_loss=.1,
            component_remanufacturing_efficiency=.7,
            material_recycling_efficiency=.8,
            dissasembly_cost_per_piece=56.00,
            energy_cost_of_recycling_a_ton=90.00
        )

    def set_recycling_method(recycling_company:RSP, recycle:bool, remanufacture:bool):
        recycling_company.remanufacture = remanufacture
        recycling_company.recycle = recycle

        return recycling_company