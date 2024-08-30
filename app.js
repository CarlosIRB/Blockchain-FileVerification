// app.js
document.getElementById('uploadForm').onsubmit = async function (e) {
    e.preventDefault();

    // Crear un nuevo objeto FormData para enviar los archivos
    const formData = new FormData();
    const files = document.getElementById('files').files;
    for (let i = 0; i < files.length; i++) {
        formData.append('files', files[i]);
    }

    // Enviar los archivos al backend en Python
    const response = await fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData
    });
    const hashResult = await response.json();
    console.log(hashResult)
    // Conectar a la blockchain usando Web3
    alert("enviar datos a polygon")
    // Conectar a la blockchain usando Web3
    // if (window.ethereum) {
    //     await window.ethereum.request({ method: 'eth_requestAccounts' });
    //     const web3 = new Web3(window.ethereum);
        
    //     // ABI y dirección del contrato desplegado en Remix IDE
    //     const contractABI = [ /* ABI del contrato */ ];
    //     const contractAddress = 'DIRECCIÓN DEL CONTRATO';

    //     const contract = new web3.eth.Contract(contractABI, contractAddress);
    //     const accounts = await web3.eth.getAccounts();

    //     // Enviar cada hash al contrato inteligente
    //     for (let filename in hashResult) {
    //         const fileHash = hashResult[filename];
    //         await contract.methods.guardarHash(filename, fileHash).send({ from: accounts[0] });
    //     }

    //     document.getElementById('hashResult').innerText = 'Hashes guardados en la blockchain!';
    // } else {
    //     console.error('Ethereum wallet no detectada');
    // }
}
