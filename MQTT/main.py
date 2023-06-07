from multiprocessing import Process
from flask import Flask
from Api.Mqtt_api import mqtt_api
import mqtt_client.mqtt_pub_sub as mqtt_pub_sub

app = Flask(__name__)

app.register_blueprint(mqtt_api, url_prefix='/mqtt_api')

def metro_state_update_process():
    client = mqtt_pub_sub.create_connection()
    mqtt_pub_sub.pull_metro_data(client)

def trainA_state_update_process():
    client = mqtt_pub_sub.create_connection()
    mqtt_pub_sub.pull_trainA_data(client)

def trainB_state_update_process():
    client = mqtt_pub_sub.create_connection()
    mqtt_pub_sub.pull_trainB_data(client)

def trainC_state_update_process():
    client = mqtt_pub_sub.create_connection()
    mqtt_pub_sub.pull_trainC_data(client)

def start_processes():
    processes = []

    metro_update_proces = Process(target=metro_state_update_process, args=())
    metro_update_proces.start()
    processes.append(metro_update_proces)

    # trainA_update_proces = Process(target=trainA_state_update_process, args=())
    # trainA_update_proces.start()
    # processes.append(trainA_update_proces)

    #trainB_update_proces = Process(target=trainB_state_update_process, args=())
    #trainB_update_proces.start()
    #processes.append(trainB_update_proces)

    #trainC_update_proces = Process(target=trainC_state_update_process, args=())
    #trainC_update_proces.start()
    #processes.append(trainC_update_proces)

    for p in processes:
        p.join()
    

if __name__ == '__main__':
    start_processes()
    app.run(debug=False, port=5001)
