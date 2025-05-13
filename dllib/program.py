def program(n):
    if n == 1:
        from . import program1_mlp_mnist as mod
    elif n == 2:
        from . import program2_mlp_cifar10 as mod
    elif n == 3:
        from . import program3_xor_dnn as mod
    elif n == 4:
        from . import program4_house_dnn as mod
    elif n == 5:
        from . import program5_cnn_mnist as mod
    elif n == 6:
        from . import program6_cnn_cifar10 as mod
    elif n == 7:
        from . import program7_rnn_books as mod
    elif n == 8:
        from . import program8_lstm_char as mod
    elif n == 9:
        from . import program9_lstm_timeseries as mod
    elif n == 10:
        from . import program10_mnist_hyper as mod
    else:
        print("Invalid program number (1–10)")
        return
    
    mod.run()
