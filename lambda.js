const net = require('net');
const AWS = require('aws-sdk');

exports.handler = async (event) => {
    const newServerPort = process.env.NEW_SERVER_PORT;
    const haproxyEndpoint = process.env.HAPROXY_ENDPOINT;
    
    const haproxyBackend = 'app-servers'
    const newServerName = 'new_server'; 
    const instanceId = event.detail['EC2InstanceId'];
    
    const ec2 = new AWS.EC2();
    const instanceDesc = await ec2.describeInstances([instanceId]).promise();
    const newServerIp = instanceDesc.Reservations[0].Instances[0].PrivateIpAddress;
    // Construct the HAProxy stats command to add a new server
    const command = `add server ${haproxyBackend}/${newServerName} ${newServerIp}:${newServerPort}`;
    // Create a socket connection to the HAProxy stats socket
    
    const client = new net.Socket();
    return new Promise((resolve, reject) => {
        client.connect(haproxyEndpoint, () => {
            console.log('Connected to HAProxy stats socket');
            client.write(`${command}\n`);
        });

        client.on('data', (data) => {
            console.log(`Received: ${data}`);
            client.end();
            resolve('Server added successfully');
        });

        client.on('error', (err) => {
            console.error(`Error: ${err}`);
            client.destroy();
            reject('Error adding server to HAProxy');
        });
    });
};