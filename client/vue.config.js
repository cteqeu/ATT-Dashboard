const path = require("path");

module.exports = {
    transpileDependencies: [
        'vuetify',
    ],
    outputDir: "../server/public",
    indexPath: path.resolve(__dirname, '../../dist/index.html'),
    assetsDir: path.resolve(__dirname, '../../dist'),
};
