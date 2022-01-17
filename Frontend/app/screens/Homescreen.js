import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, Image } from 'react-native';
import DodajKsiazkec1 from 'DodajKsiazkec1';

export default function App() {
    return (
        <View style={styles.container}>
            <Image source={require("book1.jpg")} />
            <Text>BookFinder !</Text>
            <Button 
                title="ZnajdŸ swoj¹ now¹ ulubion¹ ksi¹¿kê!"
            />
            <Button
                onPress={<DodajKsiazkec1 />}
                title="Nie widzisz swojej ulubionej ksi¹¿ki? Dodaj j¹!"
            />
            <StatusBar style="auto" />
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#ffff',
        alignItems: 'center',
        justifyContent: 'center',
    },
});

