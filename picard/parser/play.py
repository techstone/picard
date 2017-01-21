from parse import preparse

print preparse({
    'operators': {
        'ff': {
            '#repeat': {
                '+times': {
                    '&randint': {
                        'upper': 5
                    }
                },
                'operator': {
                    '#compose': [
                        {
                            'layer': 'Dense',
                            'config': {
                                'output_dim': 64,
                                'activation': {
                                    '&choice': {
                                        'options': ['relu', 'sigmoid']
                                    }
                                }
                            }
                        },
                        {
                            '#optional': {
                                'layer': 'Dropout',
                                'config': {
                                    'p': {
                                        '&uniform': {
                                            'low': 0,
                                            'high': .5
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        'denseOut': {
            'layer': 'Dense',
            'config': {
                'output_dim': 5,
                'activation': {
                    '&choice': {
                        'options': ['relu', 'sigmoid']
                    }
                }
            }
        }
    },
    'legs': {
        'in': {'input': {}},
        'out': {'output': {}}
    },
    'edges': [
        {
            'source': 'input',
            'target': 'ffStart',
            'operator': 'IDENTITY'
        },
        {
            'source': 'ffStart',
            'target': 'ffEnd',
            'operator': 'ff'
        },
        {
            'source': 'ffEnd',
            'target': 'output',
            'operator': 'denseOut'
        }
    ]
})
