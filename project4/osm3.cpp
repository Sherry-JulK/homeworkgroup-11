#include<iostream>
#include <string>
#include <cmath>
#include <time.h>
using namespace std;


string BinToHex(string str) {
	string hex = "";
	int temp = 0;
	while (str.size() % 4 != 0) {
		str = "0" + str;
	}
	for (int i = 0; i < str.size(); i += 4) {
		temp = (str[i] - '0') * 8 + (str[i + 1] - '0') * 4 + (str[i + 2] - '0') * 2 + (str[i + 3] - '0') * 1;
		if (temp < 10) {
			hex += to_string(temp);
		}
		else {
			hex += 'A' + (temp - 10);
		}
	}
	return hex;
}


string HexToBin(string str) {
	string bin = "";
	string table[16] = { "0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111" };
	for (int i = 0; i < str.size(); i++) {
		if (str[i] >= 'A' && str[i] <= 'F') {
			bin += table[str[i] - 'A' + 10];
		}
		else {
			bin += table[str[i] - '0'];
		}
	}
	return bin;
}


int BinToDec(string str) {
	int dec = 0;
	for (int i = 0; i < str.size(); i++) {
		dec += (str[i] - '0') * pow(2, str.size() - i - 1);
	}
	return dec;
}


string DecToBin(int str) {
	string bin = "";
	while (str >= 1) {
		bin = to_string(str % 2) + bin;
		str = str / 2;
	}
	return bin;
}


int HexToDec(string str) {
	int dec = 0;
	for (int i = 0; i < str.size(); i++) {
		if (str[i] >= 'A' && str[i] <= 'F') {
			dec += (str[i] - 'A' + 10) * pow(16, str.size() - i - 1);
		}
		else {
			dec += (str[i] - '0') * pow(16, str.size() - i - 1);
		}
	}
	return dec;
}

string DecToHex(int str) {
	string hex = "";
	int temp = 0;
	while (str >= 1) {
		temp = str % 16;
		if (temp < 10 && temp >= 0) {
			hex = to_string(temp) + hex;
		}
		else {
			hex += ('A' + (temp - 10));
		}
		str = str / 16;
	}
	return hex;
}

string padding(string str) {
	string res = "";
	for (int i = 0; i < str.size(); i += 1) {
		res += DecToHex((int)str[i]);

	}
	int res_length = res.size() * 4;
	res += "8";
	while (res.size() % 128 != 112) {
		res += "0";
	}
	string res_len = DecToHex(res_length);
	while (res_len.size() != 16) {
		res_len = "0" + res_len;
	}
	res += res_len;
	return res;
}

string LeftShift(string str, int len) {
	string res = HexToBin(str);
	res = res.substr(len) + res.substr(0, len);
	return BinToHex(res);
}

string XOR(string str1, string str2) {
	string res1 = HexToBin(str1);
	string res2 = HexToBin(str2);
	string res = "";
	for (int i = 0; i < res1.size(); i++) {
		if (res1[i] == res2[i]) {
			res += "0";
		}
		else {
			res += "1";
		}
	}
	return BinToHex(res);
}

string AND(string str1, string str2) {
	string res1 = HexToBin(str1);
	string res2 = HexToBin(str2);
	string res = "";
	for (int i = 0; i < res1.size(); i++) {
		if (res1[i] == '1' && res2[i] == '1') {
			res += "1";
		}
		else {
			res += "0";
		}
	}
	return BinToHex(res);
}

string OR(string str1, string str2) {
	string res1 = HexToBin(str1);
	string res2 = HexToBin(str2);
	string res = "";
	for (int i = 0; i < res1.size(); i++) {
		if (res1[i] == '0' && res2[i] == '0') {
			res += "0";
		}
		else {
			res += "1";
		}
	}
	return BinToHex(res);
}

string NOT(string str) {
	string res1 = HexToBin(str);
	string res = "";
	for (int i = 0; i < res1.size(); i++) {
		if (res1[i] == '0') {
			res += "1";
		}
		else {
			res += "0";
		}
	}
	return BinToHex(res);
}

char binXor(char str1, char str2) {
	return str1 == str2 ? '0' : '1';
}

char binAnd(char str1, char str2) {
	return (str1 == '1' && str2 == '1') ? '1' : '0';
}

string ModAdd(string str1, string str2) {
	string res1 = HexToBin(str1);
	string res2 = HexToBin(str2);
	char temp = '0';
	string res = "";
	for (int i = res1.size() - 1; i >= 0; i--) {
		res = binXor(binXor(res1[i], res2[i]), temp) + res;
		if (binAnd(res1[i], res2[i]) == '1') {
			temp = '1';
		}
		else {
			if (binXor(res1[i], res2[i]) == '1') {
				temp = binAnd('1', temp);
			}
			else {
				temp = '0';
			}
		}
	}
	return BinToHex(res);
}

string P1(string str) {
	return XOR(XOR(str, LeftShift(str, 15)), LeftShift(str, 23));
}

string P0(string str) {
	return XOR(XOR(str, LeftShift(str, 9)), LeftShift(str, 17));
}

string T(int j) {
	if (0 <= j && j <= 15) {
		return "79CC4519";
	}
	else {
		return "7A879D8A";
	}
}

string FF(string str1, string str2, string str3, int j) {
	if (0 <= j && j <= 15) {
		return XOR(XOR(str1, str2), str3);
	}
	else {
		return OR(OR(AND(str1, str2), AND(str1, str3)), AND(str2, str3));
	}
}

string GG(string str1, string str2, string str3, int j) {
	if (0 <= j && j <= 15) {
		return XOR(XOR(str1, str2), str3);
	}
	else {
		return OR(AND(str1, str2), AND(NOT(str1), str3));
	}
}
string extension(string str) {
	string res = str;
	for (int i = 16; i < 68; i += 1) {
		res += XOR(XOR(P1(XOR(XOR(res.substr((i - 16) * 8, 8), res.substr((i - 9) * 8, 8)), LeftShift(res.substr((i - 3) * 8, 8), 15))), LeftShift(res.substr((i - 13) * 8, 8), 7)), res.substr((i - 6) * 8, 8));

	}


	for (int i = 0; i < 64; i += 1) {
		res += XOR(res.substr(i * 8, 8), res.substr((i + 4) * 8, 8));


	}

	return res;
}

string compress(string str1, string str2) {
	string IV = str2;
	string A = IV.substr(0, 8), B = IV.substr(8, 8), C = IV.substr(16, 8), D = IV.substr(24, 8), E = IV.substr(32, 8), F = IV.substr(40, 8), G = IV.substr(48, 8), H = IV.substr(56, 8);
	string SS1 = "", SS2 = "", TT1 = "", TT2 = "";

	for (int j = 0; j < 64; j++) {
		SS1 = LeftShift(ModAdd(ModAdd(LeftShift(A, 12), E), LeftShift(T(j), (j % 32))), 7);
		SS2 = XOR(SS1, LeftShift(A, 12));
		TT1 = ModAdd(ModAdd(ModAdd(FF(A, B, C, j), D), SS2), str1.substr((j + 68) * 8, 8));
		TT2 = ModAdd(ModAdd(ModAdd(GG(E, F, G, j), H), SS1), str1.substr(j * 8, 8));
		D = C;
		C = LeftShift(B, 9);
		B = A;
		A = TT1;
		H = G;
		G = LeftShift(F, 19);
		F = E;
		E = P0(TT2);

	}
	string res = (A + B + C + D + E + F + G + H);
	return res;
}

string iteration(string str) {
	int num = str.size() / 128;
	string V = "7380166F4914B2B9172442D7DA8A0600A96F30BC163138AAE38DEE4DB0FB0E4E";
	string B = "", extensionB = "", compressB = "";
	for (int i = 0; i < num; i++) {
		B = str.substr(i * 128, 128);
		extensionB = extension(B);
		compressB = compress(extensionB, V);
		V = XOR(V, compressB);
	}
	return V;
}

int main() {
	string str[1];
	str[0] = "Li Na, born on February 26, 1982 in Wuhan, Hubei Province, is a Chinese woman tennis player.Beijing 2008 Olympic Games women's singles fourth, 2011 French Open, 2014 Australian Open women's singles champion, the first Asian Grand Slam women's singles champion, the highest ranking in Asian history women's singles in the world. Graduated from Huazhong University of Science and Technology.In 1989, 6-year-old Li Na began to practice tennis. He became a professional player in 1999. At the end of 2002, Li Na went to Huazhong University of Science and Technology to study journalism.In 2004, with the encouragement and support of her husband Jiangshan, she chose to return. In 2008, Li Na won the fourth place in women's singles in Beijing Olympic Games.In 2011, Li Na won the runner-up in her first Grand Slam singles final at the Australian Open and topped the women's singles competition at the French Open.Li Na, born on February 26, 1982 in Wuhan, Hubei Province, is a Chinese woman tennis player.Beijing 2008 Olympic Games women's singles fourth, 2011 French Open, 2014 Australian Open women's singles champion, the first Asian Grand Slam women's singles champion, the highest ranking in Asian history women's singles in the world. Graduated from Huazhong University of Science and Technology.In 1989, 6-year-old Li Na began to practice tennis. He became a professional player in 1999. At the end of 2002, Li Na went to Huazhong University of Science and Technology to study journalism.In 2004, with the encouragement and support of her husband Jiangshan, she chose to return. In 2008, Li Na won the fourth place in women's singles in Beijing Olympic Games.In 2011, Li Na won the runner-up in her first Grand Slam singles final at the Australian Open and topped the women's singles competition at the French Open.Li Na, born on February 26, 1982 in Wuhan, Hubei Province, is a Chinese woman tennis player.Beijing 2008 Olympic Games women's singles fourth, 2011 French Open, 2014 Australian Open women's singles champion, the first Asian Grand Slam women's singles champion, the highest ranking in Asian history women's singles in the world. Graduated from Huazhong University of Science and Technology.In 1989, 6-year-old Li Na began to practice tennis. He became a professional player in 1999. At the end of 2002, Li Na went to Huazhong University of Science and Technology to study journalism.In 2004, with the encouragement and support of her husband Jiangshan, she chose to return. In 2008, Li Na won the fourth place in women's singles in Beijing Olympic Games.In 2011, Li Na won the runner-up in her first Grand Slam singles final at the Australian Open and topped the women's singles competition at the French Open.Li Na, born on February 26, 1982 in Wuhan, Hubei Province, is a Chinese woman tennis player.Beijing 2008 Olympic Games women's singles fourth, 2011 French Open, 2014 Australian Open women's singles champion, the first Asian Grand Slam women's singles champion, the highest ranking in Asian history women's singles in the world. Graduated from Huazhong University of Science and Technology.In 1989, 6-year-old Li Na began to practice tennis. He became a professional player in 1999. At the end of 2002, Li Na went to Huazhong University of Science and Technology to study journalism.In 2004, with the encouragement and support of her husband Jiangshan, she chose to return. In 2008, Li Na won the fourth place in women's singles in Beijing Olympic Games.In 2011, Li Na won the runner-up in her first Grand Slam singles final at the Australian Open and topped the women's singles competition at the French Open.Li Na, born on February 26, 1982 in Wuhan, Hubei Province, is a Chinese woman tennis player.Beijing 2008 Olympic Games women's singles fourth, 2011 French Open, 2014 Australian Open women's singles champion, the first Asian Grand Slam women's singles champion, the highest ranking in Asian history women's singles in the world. Graduated from Huazhong University of Science and Technology.In 1989, 6-year-old Li Na began to practice tennis. He became a professional player in 1999. At the end of 2002, Li Na went to Huazhong University of Science and Technology to study journalism.In 2004, with the encouragement and support of her husband Jiangshan, she chose to return. In 2008, Li Na won the fourth place in women's singles in Beijing Olympic Games.In 2011, Li Na won the runner-up in her first Grand Slam singles final at the Australian Open and topped the women's singles competition at the French Open.Li Na, born on February 26, 1982 in Wuhan, Hubei Province, is a Chinese woman tennis player.Beijing 2008 Olympic Games women's singles fourth, 2011 French Open, 2014 Australian Open women's singles champion, the first Asian Grand Slam women's singles champion, the highest ranking in Asian history women's singles in the world. Graduated from Huazhong University of Science and Technology.In 1989, 6-year-old Li Na began to practice tennis. He became a professional player in 1999. At the end of 2002, Li Na went to Huazhong University of Science and Technology to study journalism.In 2004, with the encouragement and support of her husband Jiangshan, she chose to return. In 2008, Li Na won the fourth place in women's singles in Beijing Olympic Games.In 2011, Li Na won the runner-up in her first Grand Slam singles final at the Australian Open and topped the women's singles competition at the French Open.Li Na, born on February 26, 1982 in Wuhan, Hubei Province, is a Chinese woman tennis player.Beijing 2008 Olympic Games women's singles fourth, 2011 French Open, 2014 Australian Open women's singles champion, the first Asian Grand Slam women's singles champion, the highest ranking in Asian history women's singles in the world. Graduated from Huazhong University of Science and Technology.In 1989, 6-year-old Li Na began to practice tennis. He became a professional player in 1999. At the end of 2002, Li Na went to Huazhong University of Science and Technology to study journalism.In 2004, with the encouragement and support of her husband Jiangshan, she chose to return. In 2008, Li Na won the fourth place in women's singles in Beijing Olympic Games.In 2011, Li Na won the runner-up in her first Grand Slam singles final at the Australian Open and topped the women's singles competition at the French Open.Li Na, born on February 26, 1982 in Wuhan, Hubei Province, is a Chinese woman tennis player.Beijing 2008 Olympic Games women's singles fourth, 2011 French Open, 2014 Australian Open women's singles champion, the first Asian Grand Slam women's singles champion, the highest ranking in Asian history women's singles in the world. Graduated from Huazhong University of Science and Technology.In 1989, 6-year-old Li Na began to practice tennis. He became a professional player in 1999. At the end of 2002, Li Na went to Huazhong University of Science and Technology to study journalism.In 2004, with the encouragement and support of her husband Jiangshan, she chose to return. In 2008, Li Na won the fourth place in women's singles in Beijing Olympic Games.In 2011, Li Na won the runner-up in her first Grand Slam singles final at the Australian Open and topped the women's singles competition at the French Open.Li Na, born on February 26, 1982 in Wuhan, Hubei Province, is a Chinese woman tennis player.Beijing 2008 Olympic Games women's singles fourth, 2011 French Open, 2014 Australian Open women's singles champion, the first Asian Grand Slam women's singles champion, the highest ranking in Asian history women's singles in the world. Graduated from Huazhong University of Science and Technology.In 1989, 6-year-old Li Na began to practice tennis. He became a professional player in 1999. At the end of 2002, Li Na went to Huazhong University of Science and Technology to study journalism.In 2004, with the encouragement and support of her husband Jiangshan, she chose to return. In 2008, Li Na won the fourth place in women's singles in Beijing Olympic Games.In 2011, Li Na won the runner-up in her first Grand Slam singles final at the Australian Open and topped the women's singles competition at the French Open.Li Na, born on February 26, 1982 in Wuhan, Hubei Province, is a Chinese woman tennis player.Beijing 2008 Olympic Games women's singles fourth, 2011 French Open, 2014 Australian Open women's singles champion, the first Asian Grand Slam women's singles champion, the highest ranking in Asian history women's singles in the world. Graduated from Huazhong University of Science and Technology.In 1989, 6-year-old Li Na began to practice tennis. He became a professional player in 1999. At the end of 2002, Li Na went to Huazhong University of Science and Technology to study journalism.In 2004, with the encouragement and support of her husband Jiangshan, she chose to return. In 2008, Li Na won the fourth place in women's singles in Beijing Olympic Games.In 2011, Li Na won the runner-up in her first Grand Slam singles final at the Australian Open and topped the women's singles competition at the French Open.";
	for (int num = 0; num < 1; num++) {
		cout << "原消息为: " + str[num] << endl;
		cout << endl;
		clock_t start, stop;
		start = clock();



		string paddingValue = padding(str[num]);
		string result = iteration(paddingValue);
		cout << endl;
		cout << "杂凑值：" << endl;

		for (int i = 0; i < 8; i++) {
			cout << result.substr(i * 8, 8) << "  ";
		}

		stop = clock();
		cout << endl;
		double endtime = (double)(stop - start) / CLOCKS_PER_SEC;
		std::cout << "time: " << endtime << "s" << std::endl;
		cout << endl;
		cout << endl;
	}
}
