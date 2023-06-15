import pandas as pd
import random
import re
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

interviews_df = pd.read_csv('News1.csv',encoding = "utf-8",sep=';')
spor_kelimeleri = ["Antrenman", "Atletizm", "Basketbol", "Bisiklet", "Boks","Futbol", "Golf", "Gymnastik", "Hentbol","Koşu","Masa Tenisi","Okçuluk", "Paintball", "Sörf", "Tenis", "Voleybol","Yüzme", "Amerikan Futbolu", "Badminton", "Baseball", "Beyzbol", "Bilardo", "Body Building" "Bowling", "Boxing", "Dağcılık", "Dalgıçlık", "Dans", "E-Spor", "Fitness", "Golf ", "Güreş", "Halter", "Haltere", "Hava Sporları", "Hokey", "İp Atlama", "Jimnastik", "Kayak", "Kick Boks", "Kondisyon", "Kung Fu","Motorsiklet Yarışları", "Paintball ", "Parkour", "Ralli", "Rüzgar Sörfü","Satranç", "Scuba Diving", "Spor Salonları", "Taekwondo", "Takım Sporları", "Trambolin", "Triatlon", "Vale Tudo", "Voleybol ", "Yelken","Yüzme ","Aerobik", "Atıcılık", "Avrupa Futbolu", "Bale", "Bando", "Basketbol ", "Beşiktaş Jimnastik Kulübü", "Beyzbol","Bisiklet ", 'File', 'Puan', 'Set', 'Maç', 'Olimpiyat', 'Dünya Kupası', 'Şampiyonlar Ligi', 'Lig', 'Şampiyona', 'Kupa', 'Gol', 'Basket', 'Kart', 'Madalya', 'Sporcu', 'Maç', "Top","Kale","Pota","Forma","Koşu bandı","Antreman","Doping","Derbi ","Deplasman","Oyuncu","Takım ","Turnuva","Ofsayt","Faul","Korner","Taç","Blok","Turnike","Sporcu","Antranör","Hakem","Puan","Forma","Sezon","Fenerbahçe","Galatasaray","Beşiktaş","Milli Takım","Avrupa ligi","Trabzonspor","Kart","teknik","sezon","türkiye" ,"takım","spor","başkan","transfer","direktör","puan","oyuncu","f.bahçe","g.saray","yıldız","yönetim","dünya kupası"]   
spor_kelimeleri = [kelime.lower() for kelime in spor_kelimeleri]
bilisim_kelimeleri = ['Bilgisayar', 'Yazılım', 'Donanım', 'Programlama', 'Algoritma', 'Veri', 'Veritabanı', 'Ağ', 'İnternet', 'Web', 'Mobil', 'Geliştirme', 'Fonksiyon', 'Değişken', 'Döngü', 'Kodlama', "İşletim sistemi", 'Linux', 'Windows', 'MacOS', 'IOS', 'Android', 'Yapay zeka', 'Makine öğrenmesi', 'Derin öğrenme', 'Doğal dil işleme', 'Veri madenciliği', 'Blok zinciri', 'Kriptopara', 'Güvenlik', 'Hack', 'Siber saldırı', 'Firewall', 'Antivirüs', 'Şifreleme', 'HTTPS', 'ağ', 'algoritma', 'altyapı', 'analiz', 'animasyon', 'API', 'arayüz',  'bağlantı', 'bağlantı noktası', 'bağımsız değişken','bilgisayar ','sunucu', 'sunucu arabirimi', 'tarayıcı', 'teknoloji', 'uygulama', 'veri', 'veri yönetimi', 'web', 'web uygulaması', "algoritma", "veri yapıları", "yapay zeka", "derin öğrenme", "doğal dil işleme", "veri madenciliği", "ağ programlama", "veri tabanı yönetimi", "siber güvenlik", "şifreleme", "yazılım geliştirme", "web geliştirme", "mobil uygulama", "blok zinciri", "big data","robotik", "otomasyon", "yapay sinir ağları", "makine öğrenmesi", "veri analitiği", "ağ güvenliği", "bilgisayar ağları", "programlama dilleri","sayısal devreler", "bulut depolama", "sanallaştırma", "ağ yönetimi", "veri yönetimi", "veri ambarı","uygulama entegrasyonu","işletim sistemleri", "veri saklama", "bulut hizmetleri", "proje yönetimi", "iş analitiği", "veri görselleştirme", "iş zekası", "veri modelleme","optimizasyon", "destek vektör makineleri", "karar ağaçları", "k-NN", "neural nets", "klasifikasyon", "kümeleme", "doğrusal regresyon", "kullanıcı arayüzü tasarımı", "UI/UX tasarımı", "web tasarımı", "arayüz geliştirme", "web uygulama güvenliği", "siber saldırılar", "hacker","sızma","sistem","web","iletişim","bulut","bilişim","mobil"]
bilisim_kelimeleri = [kelime.lower() for kelime in bilisim_kelimeleri]

def clean_text(text):
	# Küçük harfe çevirme
	text = text.lower()
	# Noktalama işaretlerini ve sayıları kaldırma
	text = re.sub('[%s]' % re.escape(string.punctuation + '0123456789'), '', text)
	# Tekrar eden boşlukları kaldırma
	text = re.sub('\s+', ' ', text)

	return text.strip()    
def remove_stopwords(text):
	# Türkçe stop word'leri yükleme
	stopwords_list = stopwords.words('turkish')
	text=clean_text(text)
	# Metni kelimelere ayırma
	words = text.split()
	# Stop word'leri kaldırma
	words = [word for word in words if word.lower() not in stopwords_list]
	# Kaldırılan stop word'leri yeniden birleştirme
	text = ' '.join(words)
	return text


def generete_population(population_size,birey_uzunlugu):
	population = []
	for i in range(population_size):
		population.append(Birey(birey_uzunlugu))
	return population


class Birey:
    def __init__(self, birey_uzunlugu):
        self.bilisim = []
        self.spor = []
        self.fitness_value = 0
        #random.seed(66)  
        for i in range(birey_uzunlugu):
            kelime = random.choice(bilisim_kelimeleri)
            self.bilisim.append(kelime)
        for i in range(birey_uzunlugu):
            kelime = random.choice(spor_kelimeleri)
            self.spor.append(kelime)
        self.succes_count = 0
        self.fail_count = 0

    def detect_class(self, words):
        spor_count, bilisim_count = 0, 0
        for word in words:
            if word in self.spor:
                spor_count += 1
            if word in self.bilisim:
                bilisim_count += 1
        if spor_count > bilisim_count:
            return "spor"
        elif spor_count < bilisim_count:
            return "bilisim"
        else:
            return random.choice(["spor", "bilisim"])

        
def compute_fitness_values():
    fitness_values = []
    for birey in population:
        succes_count = 0
        fail_count = 0
        for interview in interviews:
            if birey.detect_class(interview.words) == interview.category:
                succes_count += 1
            else:
                fail_count += 1
        fitness_value = succes_count / (succes_count + fail_count)
        birey.fitness_value = fitness_value
        fitness_values.append(fitness_value)
    return fitness_values

		
# Random seçim işlemi
def selection(population, fitness_values):
		# Seçilen iki bireyin indekslerini saklamak için iki boş liste oluşturun
		selected_indices = []
		# İlk birey için seçim
		index1 = random.choices(range(len(population)), weights=fitness_values)[0]
		selected_indices.append(index1)
		# İkinci birey için seçim
		index2 = random.choices(range(len(population)), weights=fitness_values)[0]
		# İndexlerin farklı olmasını sağlamak için döngü kullanarak tekrar seçim yapın
		while index2 == index1:
				index2 = random.choices(range(len(population)), weights=fitness_values)[0]
		selected_indices.append(index2)
		return selected_indices

	
def mutate(mutation_rate):
	for person in population:
		for i in range(len(person.spor)*mutation_rate//100):
			spor_mutate_idx= random.randint(0,len(person.spor)-1)
			random_spor=random.choice(spor_kelimeleri)
			while random_spor in person.spor:
				random_spor=random.choice(spor_kelimeleri)
		
			random_bilisim=random.choice(bilisim_kelimeleri)
			while random_bilisim in person.bilisim:
				random_bilisim=random.choice(bilisim_kelimeleri)

			bilisim_mutate_idx= random.randint(0,len(person.bilisim)-1)
			person.spor[spor_mutate_idx]=random_spor
			person.bilisim[bilisim_mutate_idx]=random_bilisim
		
# Crossover işlemi
def crossover(selected_indices):
		# Seçilen bireylerin indekslerini alın
		
		index1, index2 = selected_indices[0], selected_indices[1]
		# Crossover noktası rastgele seçilsin
		crossover_point = random.randint(0, len(population[index1].spor)-1)
		# Yeni bireyleri oluşturmak için crossover işlemi yapın
		birey1=population[index1]
		birey2=population[index2]

		tmp1spor= birey1.spor[:crossover_point] + birey2.spor[crossover_point:]
		tmp2spor= birey2.spor[:crossover_point] + birey1.spor[crossover_point:]
		tmp1bilisim= birey1.bilisim[:crossover_point] + birey2.bilisim[crossover_point:]
		tmp2bilisim= birey2.bilisim[:crossover_point] + birey1.bilisim[crossover_point:]
		
		birey1.spor=tmp1spor
		birey2.spor=tmp2spor
		birey1.bilisim=tmp1bilisim
		birey2.bilisim=tmp2bilisim
        
class Interview:
    def __init__(self,words,category):
        self.words=words
        self.category=category
        


#1. Population 2 
#2. Population 16
#3. Population 100
#4. Mutation 2
#5. Mutation 8
#6. Mutation 100S

population_size=16
word_count=16
interview_count=200
mutation_rate=8
population=generete_population(population_size,word_count)
threshold=0.75
interviews=[]

#random.seed(123)  

for i in range(interview_count):
    idx = random.choice(range(len(interviews_df["Content"])))
    content = interviews_df["Content"][idx]
    category = interviews_df["Category"][idx]
    words = remove_stopwords(content).split()
    interviews.append(Interview(words, category))


fitness_values=compute_fitness_values()
max_fitness=max(fitness_values)
print(max_fitness)
print(fitness_values)
max_fitness_valuess=[]
max_fitness_valuess.append(max_fitness)

i=0
limit=40
while max_fitness < threshold and i < limit:

    # Random selection ve crossover işlemlerini gerçekleştirin
    for j in range(population_size//2):  # 4 çift yeni birey oluşturun
        selected_indices = selection(population, fitness_values)
        crossover(selected_indices)

    mutate(mutation_rate)

    for birey in population:
        birey.succes_count = 0
        birey.fail_count = 0

    i = i + 1
    fitness_values = compute_fitness_values()
    max_fitness = max(fitness_values)
    max_fitness_valuess.append(max_fitness)
    print(max_fitness)
    print(fitness_values)

    
    
#print best situtations word list
print("-------PARAMETRE DEĞERLERİ / GRAFİK VE EN İYİ BİREYİN İÇERDİĞİ KELİMELER -------")

print("Popülasyon büyüklüğü:",population_size)
print("Her bireydeki kelime sayısı:",word_count*2)
print("Kategorisi tahmin edilecek yorum sayısı: ",interview_count)
print("Mutasyon oranı:",mutation_rate)
print("Elde edilmesi istenen başarı değeri:",threshold)
print("-----------------------------------")

max_birey = max(population, key=lambda p: p.fitness_value)

print("En iyi bireyin içerdiği spor kelimeleri:" ,max_birey.spor)
print("-----------------------------------")
print("En iyi bireyin içerdiği bilişim kelimeleri:" ,max_birey.bilisim)

import matplotlib.pyplot as plt

plt.plot(max_fitness_valuess)
plt.axhline(y=max(max_fitness_valuess), color='r', linestyle='-')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.title('Fitness vs Generation')
plt.show()

