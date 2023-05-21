# Delivery Tracking System

This project contains codes for a delivery tracking system

## prerequisite/setup

- Install Docker on your machine

## How to test

- Pull the code from into your local computer
- change directory into the `api/` for the repo root

    ```{bash}
    cd api/
    ```

- Run the test using the command below. This code runs the prepared bash script that makes it easy to test the codes.

    ```{bash}
    bash run-test.sh
    ```

`Note` after running all the above steps the code should pass meaning that all is great and good to go.

## How to run

- To run locally use the command below

    ```{bash}
    sudo docker-compose up --build
    ```

- To cancel or stop running use the command below

    ```{bash}
    Ctrl + C
    ```

- To stop all the running containers in the background

    ```{bash}
    docker-compose down
    ```

## Step to build and deploy into production

- Create a PR on Github a `test` workflow runs an automated test

- After the automated test is completed and the code is merged another `build` workflow kick in to build docker images deploy them to the docker hub and step up connect to the digital ocean, and connect to a Kubernetes context on the digital ocean. Deploy the service. When successful the application who all be live.
`Note` I did not complete the part of the pipeline to get this done but the code Kubernetes code for creating and deploying the resource is in this repo and they work. **It is difficult to make only payments in Nigeria. So I could not open a free account.**

## API Analysis

### Create shipment `POST api/v1/dts/shipment/`

Helps create a shipment before being tracked and handed over to dispatchers

### Get shipment `GET api/v1/dts/shipment/?waybill_no=<waybill_no>`

Helps to get information about a single shipment

### List all shipments `GET api/v1/dts/shipments/?is_completed=false&page=1&per_page=1`

Helps to list all and filter all the shipments created by the courier company

### Advance Shipment info `GET api/v1/dts/shipment-info/?waybill_no=<waybill_no>`

Helps to get more advanced data on a given shipment. This return both the shipment data and the tracking logs.

### Tracking Shipment `POST api/v1/dts/move-shipment/{waybill_no}`

When a shipment is created by a dispatch company the endpoint would be called:

- For initial assignment of shipment by the courier (e.g. in a warehouse) to a dispatcher
- When the dispatcher is in-transit all with the location before going on to the road
- When the shipment is taken to another warehouse
- When the shipment is given to another dispatcher

`Note`: This endpoint tracks the entire life cycle of the shipment

### Cancel Shipment `PUT api/v1/dts/cancel-shipment/`

Help to cancel shipment i.e no tracking of the shipment would be done or continued

### End Shipment `PUT api/v1/dts/end-shipment/`

This endpoint would be called to help complete a shipment, i.e., when it has been delivered to the receiver.

### Delete shipment `DELETE api/v1/dts/shipment/`

Helps to delete a shipment from the system. Useful when courier inputs wrong data into their system

