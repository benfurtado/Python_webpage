
function startScan() {
    fetch('/start_scan')
        .then(response => {
            if (response.ok) {
                console.log('Barcode scanning started.');
            } else {
                console.error('Failed to start barcode scanning.');
            }
        })
        .catch(error => {
            console.error('Error starting barcode scanning:', error);
        });
}

function stopScan() {
    fetch('/stop_scan')
        .then(response => {
            if (response.ok) {
                console.log('Barcode scanning stopped.');
                window.location.href = document.referrer; //to go back to the previous tab
            } else {
                console.error('Failed to stop barcode scanning.');
            }
        })
        .catch(error => {
            console.error('Error stopping barcode scanning:', error);
        });
    }