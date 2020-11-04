module.exports = {
    root: true,
    env: {
        node: true,
    },
    extends: ['plugin:vue/essential', '@vue/airbnb', '@vue/typescript/recommended'],
    parserOptions: {
        ecmaVersion: 2020,
    },
    rules: {
        indent: ['error', 4],
        'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        'object-curly-newline': 'off',
        'import/extensions': 'off',
    },
    settings: {
        'import/resolver': {
            node: {
                extensions: ['.js', '.vue', 'ts'],
            },
        },
    },
};
