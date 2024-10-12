import App from './components/app.js'

window.onload = () => {
    console.log('app')
    let app = new App(['192.168.31.1', '172.68.8.3', '1.1.1.1', '8.8.8.8'])
    app.init()
    app.render()
}