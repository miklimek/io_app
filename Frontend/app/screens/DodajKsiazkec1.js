import React, { useState, useEffect } from "react";
import { Keyboard, Text, TextInput, StyleSheet, View } from "react-native";

const Example = () => {
    const [keyboardStatus, setKeyboardStatus] = useState(undefined);

    useEffect(() => {
        const showSubscription = Keyboard.addListener("keyboardDidShow", () => {
            setKeyboardStatus("");
        });
        const hideSubscription = Keyboard.addListener("keyboardDidHide", () => {
            setKeyboardStatus("WprowadŸ tekst");
        });

        return () => {
            showSubscription.remove();
            hideSubscription.remove();
        };
    }, []);

    return (
        <View style={style.container}>
            <TextInput
                style={style.input}
                placeholder='Dodaj tytó³'
                onSubmitEditing={Keyboard.dismiss}
            />

            <TextInput
                style={style.input}
                placeholder='Dodaj autora'
                onSubmitEditing={Keyboard.dismiss}
            />

            <TextInput
                style={style.input}
                placeholder='Dodaj opis ksi¹¿ki'
                onSubmitEditing={Keyboard.dismiss}
            />
            <Text style={style.status}>{keyboardStatus}</Text>
        </View>
    );
}

const style = StyleSheet.create({
    container: {
        flex: 1,
        padding: 36
    },
    input: {
        padding: 10,
        borderWidth: 0.5,
        borderRadius: 4
    },
    status: {
        padding: 10,
        textAlign: "center"
    }
});

export default Example;