tag: v2.21.0
name: TensorFlow 2.21.0
published_at: 2026-03-06T19:48:15Z
prerelease: False

# Release 2.21.0

## TensorFlow

### Breaking Changes

* Support for Python 3.9 has been removed starting with TF 2.21.
* The TensorBoard (TB) dependency has been removed starting with TF 2.21.

### Major Features and Improvements

* `tf.lite`
    * Adds int8 and int16x8 support for SQRT operator.
    * Adds int16x8 support for EQUAL and NOT_EQUAL operators.
    * Adds support for int2 type.
    * Adds support for int2/int4 in tfl.cast .
    * Adds support for SRQ int2 in tfl.fully_connected.
    * Adds support for int4 in tfl.slice.
    * Adds support for uint4 type.

*  `tf.image`
    * Adds JPEG XL support in decode_image.

### Bug Fixes and Other Changes

* `tf.data`
    * Adds `NoneTensorSpec` to the public API so that `None`s in `element_spec`
      can be identified via `isinstance(..., tf.NoneTensorSpec)`.

## Thanks to our Contributors

This release contains contributions from many people at Google, as well as:

Aaraviitkgp, Abhijeet, Abhinav Gunjal, Abhishek, Adam Paszke, Aditya Gupta, Aditya Jha, Aditya Sharma, Adrian Kuegel, Aiden Grossman, Akarsh, Akhil Goel, Alan Kelly, Aleksa Arsic, Aleksei, Aleksei Nurmukhametov, Alex, Alexander Belyaev, Alexander Grund, Alexander Lyashuk, Alexander Shaposhnikov, Alex Pivovarov, Aliia Khasanova, Alina Sbirlea, Allan Renucci, Amelia Thurdekoos, Amit Sabne, Andrei Ivanov, Andrew Dame, Andrey Portnoy, Anish Nair, Anlun Xu, Antonio Sanchez, anuj chincholikar, Anuj Chincholikar, Aravindh Balaji, aravindhbalaji1985, Arian Arfaian, Armin Felder, Artem Belevich, Ashish Rao, Ashitesh Singh, A. Unique TensorFlower, Bart Chrzaszcz, benediktjohannes, Benjamin Chetioui, Benjamin Kramer, Berkin Ilbeyi, Bhatu, Bhavani Subramanian, Bhupendra Dubey, Bill Varcho, Bixia Zheng, Blake Hechtman, Bodhi Silberling, BruceXinXin, Bryan Massoth, Buddh Prakash, Byungchul Kim, Ce Zheng, Changhui Lin, Chao, Charles Alaras, Chase Riley Roberts, Chenhao Jiang, Chris Ashton, Chris Jones, Chris Kennelly, Christian Sigg, Chuan He, Chunlei Niu, Chun-nien Chan, Chunyu Jin, Clive Verghese, Cong Liu, Corentin Kerisit, Daniel Chen, Daniel Kuts, Daniel Ng, Daniel Sosa, Daniel Suo, Danila Malyutin, David Dunleavy, David Majnemer, David Pizzuto, Deepika Rajani, deeptanshusekhri, dependabot[bot], Deqiang Chen, Derek Murray, Dillon Sharlet, Dimitar (Mitko) Asenov, Dimitris Vardoulakis, Dirk Hornung, DottsGit, Dragan Mladjenovic, Eetu Sjöblom, Elen Kalda, Emilio Cota, Emily Fertig, Eugene Zhulenev, Eusebio Durán Montaña, Evan Brown, Ezekiel Calubaquib, Faijul Amin, Felix Wang, Fengwu Yao, Fergus Henderson, Frederic Rechtenstein, Frederik Gossen, Gabriel Gerlero, Gagan Nagaraj, gaikwadrahul8, garry00107, gaurides, George Pawelczak, Georg Stefan Schmid, gns, Goran Flegar, Graham, Grant Jensen, Greg Olechwierowicz, Gregory Pataky, Grzegorz Gawryał, Gunhyun Park, guozhong.zhuang, Haibo Huang, Hana Joo, Hariprasad Ravishankar, Harsha H S, Harshit Monish, Henning Becker, Hittanshu, Hoeseong (Hayden) Kim, Hugo Mano, Hyeontaek Lim, Ibrahim Umit Akgun, ILCSFNO, Ilia Sergachev, Ilya Tikhonovskiy, Iman Hosseini, Ionel Gog, Isha Arkatkar, isharif168, Ivo Ristovski List, Jacques Pienaar, Jae H. Yoo, Jaeyoon Jung, Jake Harmon, James Hilliard, jameslovespancakes, James Spooner, Jane Liu, Jaroslav Sevcik, Jeff Parker, Jeffrey A. Dean, Jeremy Meredith, Jialei Chen, Jian Cai, Jian Li, Jie Luo, Jim Lin, Jing Pu, Jinliang Wei, Jiya Zhang, Joel Wee, Johannes Buchner, Johannes Reifferscheid, Johnny, Jorge Gorbe Moya, Joshua Lang, Joshua Wang, Joss Briody, jparkerh, Juanli Shen, Juhyun Lee, Jun Jiang, Junwhan Ahn, Kadir Barut, Kanglan Tang, Kanish Anand, Kanvi Khanna, Karlo Basioli, Ken Franko, Kevin Chen, Kevin Gleason, Kingston Mandisodza, Koki Ibukuro, Kostiantyn Liepieshov, Krishna Haridasan, Krishna Somani, Krzysztof Kosiński, Kuy Mainwaring, lambert, Larry Lansing, Lin Chai, Lord ε Rebel, Luke Baumann, Luke Hutton, madhavmadupu, Majid Dadashi, Mani Ananth, Manjunath Gaonkar, Marcello Maggioni, Marcin Radomski, Maria Lyubimtseva, Marissa Ikonomidis, Mark Daoust, Mason Chang, Matej Aleksandrov, Mateusz Sokół, Matthias Guenther, Matthias Kramm, Matt Hurd, Matt Kreileder, Maxime France-Pillois, Maxim Ermilov, Mehrdad Khani, Melissa Weber Mendonça, MERT-CKR, Michael Goldfarb, Michael Green, Michael Kuperstein, Michael Voznesensky, Michael Whittaker, Mihai Maruseac, Mikhail Goncharov, Ming-Xu Huang, Mircea Trofin, Misha Gutman, misterBart, mmakevic-amd, Mohamed AbdElmoneim, Mohamed Amine Zghal, Mohammadreza Heydary, Mohammed Anany, mraunak, Mudit Gokhale, Nayana Thorat, Nevi, nhatle, Nhat Le, Nihar0071, Nikhil, Nikita Putikhin, Niklas Vangerow, Nitin Srinivasan, Oleg Shyshkov, Olli Lupton, Om Thakkar, Pankaj Kanwar, Parker Schuh, Paul Ganssle, Pauline Sho, Pavithra Eswaramoorthy, Pedro Gonnet, pemeliya, Penporn Koanantakool, Perry Gibson, Peter Buchlovsky, Peter Gavin, Peter Hawkins, Pham Binh, Phani Paladugula, Philipp Hack, Praneeth Mandala, Praveen Batra, psinfinity, Qingwei Zhang, Quentin Khan, Quoc Truong, QZero, Rachel Han, Raffi Khatchadourian, Ram Rachum, RasheedAli-Shaik, Raviteja Gorijala, Reed Wanderman-Milne, Reilly Grant, Renjie Wu, Richard Levasseur, Robert David, Ryan M. Lefever, Sachin M, Sagun Bajra, Sai Ganesh Muthuraman, Saksham Singh Rathore, Sannidhya Chauhan, Sayan Saha, Sean Talts, Seher Ellis, Sergei Lebedev, Sergey Kozub, Sevin Fide Varoglu, Shahriar Rouf, Shanbin Ke, Shaogang Wang, Sharad Vikram, Shawn Lu, Siddhartha Menon, Siqiao Wu, skill, Smit Hinsu, snadampal, Sohaib Iftikhar, Soowon Jeong, spiao, Srijan Upadhyay, stevemcgregory, Subham Soni, Subhankar Shah, Swachhand Lokhande, Tai Ly, TensorFlower Gardener, Terry Heo, Terry Sun, Terry Tao, Theotime Combes, Thomas Joerg, Thomas Köppe, Tiago Quelhas, TJ Xu, Toli Yevtushenko, Tomás Longeri, Tom Hennigan, Tommy Chiang, Tom Natan, Tongfei Guo, Tori Baker, Uwe L. Korn, Vadym Matsishevskyi, Vamsi Manchala, Venkat6871, Victor Stone, Ville Vesilehto, Vitalii Dziuba, Vladimir Belitskiy, Vlad Sytchenko, Volodymyr Kysenko, Wai Hon Law, wan3x, Weiyi Wang, Will Froom, William S. Moses, wondertx, Xuefei Jiang, Yang Chen, Yash Katariya, Yasir Ashfaq, yasiribmcon, Yeou Chiou, Yicheng Luo, Yi Kong, Yimei Sun, Yin Zhang, Yuchen Yao, Yue Sheng, Yulia Baturina, Yunjie Xu, Yunlong Liu, Yun Peng, Yurii Topin, Zac Cranko, Zac Mustin, Zenong Zhang, Zeyu Wang, Zhanyong Wan, Zixuan Jiang, Ziyin Huang, Zviki Nozadze