# Target interface
class IndianSwitchBoard:
    def provide_power_230v(self):
        pass

# Adaptee class (different interface)
class USPhoneCharger:
    def charge_110v(self):
        return "Charging phone with 110V power"

# Adapter class
class IndianPortAdapter(IndianSwitchBoard):
    def __init__(self, us_phone_charger):
        self.us_phone_charger = us_phone_charger

    def provide_power_230v(self):
        # Simulate converting 230V to 110V for the US charger
        print("Adapting 230V Indian power to 110V for US charger...")
        return self.us_phone_charger.charge_110v()

# Usage
if __name__ == "__main__":
    # Create a USPhoneCharger instance
    us_charger = USPhoneCharger()

    # Create an adapter to make USPhoneCharger compatible with IndianSwitchBoard
    adapter = IndianPortAdapter(us_charger)

    # Use the adapter with the Indian switchboard
    print(f"Power status: {adapter.provide_power_230v()}")