import os 
import psutil
import time
from playsound import playsound

def menu():
    print("[1] Starta övervakningsläge")
    print("[2] Visa systemstatus")
    print("[3] Skapa larm")
    print("[4] Visa larm")
    print("[5] Starta övervakning")
    print("[0] Avsluta programmet.")

def get_cpu_usage():
    return psutil.cpu_percent()

def get_ram_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('C:').percent


def monitor_system(cpu_threshold, ram_threshold, disk_threshold):

  try: 
    while True: 
       cpu_usage = get_cpu_usage()
       ram_usage = get_ram_usage()
       disk_usage = get_disk_usage()

       print(f"CPU usage, CPU stats: {cpu_usage}%")
       print(f"RAM Usage: {ram_usage}%")
       print(f"Disk usage: {disk_usage}%")
       print("-" * 30)
    
       if cpu_usage > cpu_threshold:
                print(f"ALARM: CPU-användning över gränsen! ({cpu_usage}%)")
                playsound('alarm.mav')
       if ram_usage > ram_threshold:
                print(f"ALARM: RAM-användning över gränsen! ({ram_usage}%)")
                playsound('alarm.mav')
       if disk_usage > disk_threshold:
                print(f"ALARM: Disk-användning över gränsen! ({disk_usage}%)")
                playsound('alarm.mav')

       time.sleep(3)
        # Option to return to the main menu
       if input("Tryck 'm' för att återgå till huvudmenyn, eller valfri tangent för att fortsätta: ").lower() == 'm':
                break
  except KeyboardInterrupt:
    print ("monitoring stopped.")

def main():
    thresholds = {"CPU": None, "RAM": None, "Disk": None}
    övervakning_aktiv = False
    while True:
        menu()
        option = int(input("Select your option: "))
        
        if option == 1:
            övervakning_aktiv = True
            print("Starting system monitoring...")
        elif option == 2:
            if övervakning_aktiv == True:
                print(f"CPU Usage: {get_cpu_usage()}%")
                print(f"RAM Usage: {get_ram_usage()}%")
                print(f"Disk Usage: {get_disk_usage()}%")
            else:
               print("övervakningen EJ startad. Tryck 1 för att starta Övervakning.")
        elif option == 3:
            thresholds["CPU"] = float(input("Ange CPU-alarmgräns (i %): "))
            thresholds["RAM"] = float(input("Ange RAM-alarmgräns (i %): "))
            thresholds["Disk"] = float(input("Ange Disk-alarmgräns (i %): "))
            print("Larmgränser inställda.")
        elif option == 4:
            if all(thresholds.values()):
                print("Nuvarande larmgränser:")
                print(f"CPU: {thresholds['CPU']}%")
                print(f"RAM: {thresholds['RAM']}%")
                print(f"Disk: {thresholds['Disk']}%")
            else:
                print("Inga larmgränser inställda än.")
        elif option == 5:
            if övervakning_aktiv:
                if None in thresholds.values():
                    print("Ställ in larmgränser innan du startar övervakning.")
                else:
                    print("Startar systemövervakning...")
                    monitor_system(thresholds["CPU"], thresholds["RAM"], thresholds["Disk"])
            else:
                print("Övervakningen EJ startad. Tryck 1 för att starta övervakning.")
        elif option == 0:
            print("Tack för att du använde programmet. Hejdå.")
            break
        else:    
            print("Ogiltigt alternativ. Försök igen.")    

if __name__ == "__main__":
    main()