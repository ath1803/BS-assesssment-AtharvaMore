from flask import Flask ,jsonify, request
import subprocess
import os
import platform

app = Flask(__name__)

@app.route('/')
def home():
    return "Browserstack Test"


@app.route('/start', methods=['POST'])
def start_test():
    data = request.get_json()
    browser = data.get("browser")
    url = data.get("url")

    if not browser or not url:
        return "Browser and URL is required"
    
    try:
        system = platform.system()
        if platform.system() == 'Windows':
            if browser.lower() == "chrome":
                subprocess.Popen(["start" ,"chrome" ,url],shell=True)
            elif browser.lower() == "firefox":
                subprocess.Popen(["start" ,"firefox" ,url],shell=True)
            else:
                return jsonify({"error": "Enter a Valid Browser"}),500
        
        return jsonify({"message": "Browser opened successfully with the requested url"}),200
    except Exception as e:
        return jsonify({"error": str(e)}),500

@app.route('/stop', methods=['POST'])
def stop_test():
    data = request.get_json()
    browser = data.get("browser")

    if not browser:
        return "Browser is required"
    
    try:
        
        system = platform.system()
        if platform.system() == 'Windows':
            if browser.lower() == "chrome":
                subprocess.call("taskkill /f /im chrome.exe",shell=True)
            elif browser.lower() == "firefox":
                subprocess.call("taskkill /f /im firefox.exe",shell=True)
            else:
                return jsonify({"error": "Enter a Valid Browser"}),500
        
        return jsonify({"message": "Browser Closed Successfully"}),200
    
    except Exception as e:
        return jsonify({"error": str(e)}),500

@app.route('/clean', methods=['POST'])
def clean_test():
    data = request.get_json()
    browser = data.get("browser")

    if not browser:
        return "Browser is required"
    
    try:
        
        system = platform.system()
        if platform.system() == 'Windows':
            if browser.lower() == "chrome":
                profile_path = r"C:\Users\hp\AppData\Local\Google\Chrome\User Data\Profile 5"
            
                dataToDelete = ["History", "Cache", "Cookies", "Downloads", "Saved Passwords","Sessions","Top Sites","Visited Links"]

                deletedData=[]

                for i in dataToDelete:
                    data_path = os.path.join(profile_path,i)
                    if os.path.exists(data_path):
                        try:
                            if os.path.isFile(data_path):
                                os.remove(data_path)
                            else:
                               

                               subprocess.call(f'rmdir /s /q "{data_path}"', shell = True)


                            deletedData.append(i)  


                        except Exception as e:
                            continue

                return jsonify({
                "message" : f"Data Cleared from Chrome",
                "deleted data" : deletedData}),200
            
            if browser.lower()== "firefox":
                profile_path = r"C:\Users\hp\AppData\Roaming\Mozilla\Firefox\Profiles\c6afhjhx.default-release"
            
                dataToDelete = ["History", "Cache", "Cookies", "Downloads", "Saved Passwords","Sessions","Top Sites","Visited Links"]

                # deletedData=[]

                for i in dataToDelete:
                    data_path = os.path.join(profile_path,i)
                    if os.path.exists(data_path):
                        try:
                            if os.path.isFile(data_path):
                                os.remove(data_path)
                            else:
                               

                               subprocess.call(f'rmdir /s /q "{data_path}"', shell = True)


                            # deletedData.append(i)  


                        except Exception as e:
                            continue

                return jsonify({
                "message" : f"Data Cleared from Firefox"
                
            }),200
    except Exception as e:
        return jsonify({"error": str(e)}),500        
                
                    
if __name__ == '__main__':
    app.run(debug=True)                        
                            
                        
                
                         
                    
                        
                    
            

                 




    
    

