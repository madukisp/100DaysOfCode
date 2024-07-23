const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: false, // Desativar nodeIntegration para segurança
            contextIsolation: true, // Ativar contextIsolation para segurança
            enableRemoteModule: false // Desativar remoteModule para segurança
        },
        resizable: true,
        minimizable: true,
        maximizable: true,
        frame: true
    });

    win.loadURL('https://chat.openai.com/');

    win.webContents.on('did-fail-load', () => {
        win.loadFile('index.html');
    });

    win.webContents.on('new-window', (event, url) => {
        event.preventDefault();
        win.loadURL(url);
    });

    win.webContents.on('will-navigate', (event, url) => {
        if (url !== win.webContents.getURL()) {
            event.preventDefault();
            win.loadURL(url);
        }
    });
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});
