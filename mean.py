#given a list of numbers, get the mean,
,
numbers = [35,,
4,,
-111,,
-123,,
5,,
51,,
-39,,
-62,,
-83,,
-80,,
-118,,
-110,,
16,,
53,,
-109,,
-101,,
-75,,
-72,,
-94,,
42,,
-48,,
-61,,
-7,,
-77,,
-12,,
56,,
-77,,
-124,,
-109,,
3,,
-150,,
-146,,
65,,
-13,,
23,,
65,,
1,,
-39,,
-66,,
-92,,
36,,
25,,
32,,
46,,
-68,,
22,,
-133,,
-138,,
88,,
-68,,
-16,,
45,,
-40,,
-37,,
42,,
-123,,
-104,,
-112,,
-42,,
58,,
-57,,
-44,,
-104,,
-78,,
90,,
-76,,
-89,,
16,,
37,,
-32,,
-35,,
7,,
-25,,
-65,,
-67,,
-20,,
-43,,
94,,
-60,,
-87,,
79,,
93,,
27,,
1,,
38,,
28,,
-15,,
6,,
-54,,
47,,
86,,
27,,
36,,
-40,,
-1,,
71,,
-104,,
-67,,
-33,,
-100,,
76,,
90,,
-30,,
4,,
63,,
13,,
14,,
11,,
36,,
95,,
4,,
5,,
-31,,
-65,,
31,,
-94,,
58,,
67,,
30,,
-91,,
-139,,
94,,
-71,,
-104,,
-139,,
37,,
-53,,
78,,
-114,,
1,,
-140,,
-76,,
-18,,
-121,,
22,,
-147,,
16,,
-111,,
-43,,
-144,,
-65,,
-36,,
26,,
-58,,
68,,
-3,,
45,,
-9,,
-36,,
-117,,
-79,,
90,,
-103,,
-120,,
-84,,
13,,
95,,
-143,,
-31,,
18,,
0,,
-96,,
24,,
76,,
71,,
-47,,
85,,
94,,
-55,,
39,,
-44,,
55,,
21,,
91,,
83,,
-144,,
43,,
-13,,
3,,
-80,,
-5,,
-140,,
12,,
80,,
-78,,
-145,,
-32,,
-33,,
97,,
-119,,
14,,
-18,,
89,,
77,,
-54,,
78,,
-33,,
-31,,
44,,
-122,,
-22,,
-53,,
-137,,
56,,
-21,,
-127,,
-65,,
60,,
-88,,
-124,,
94,,
25,,
-95,,
-55,,
-149,,
86,,
-6,,
6,,
-149,,
-67,,
-50,,
63,,
48,,
-57,,
-96,,
-6,,
76,,
-147,,
72,,
5,,
-27,,
49,,
14,,
-64,,
27,,
-1,,
19,,
-32,,
49,,
33,,
79,,
45,,
-115,,
61,,
-97,,
64,,
75,,
-74,,
-110,,
-61,,
-35,,
-129,,
57,,
-110,,
-9,,
-109,,
-135,,
-87,,
0,,
72,,
-22,,
-142,,
22,,
-35,,
-56,,
-133,,
73,,
95,,
24,,
-95,,
-150,,
50,,
-64,,
95,,
-85,,
87,,
7,,
16,,
-131,,
-139,,
46,,
71,,
-53,,
26,,
-6,,
-122,,
33,,
50,,
-103,,
-148,,
-15,,
-134,,
54,,
52,,
-121,,
8,,
-106,,
-81,,
96,,
-106,,
-93,,
63,,
-123,,
-147,,
-31,,
-116,,
-116,,
-106,,
67,,
-148,,
-110,,
63,,
94,,
4,,
25,,
-33,,
85,,
21,,
-36,,
-59,,
-104,,
-80,,
-31,,
-138,,
97,,
70,,
26,,
49,,
78,,
-56,,
91,,
-126,,
19,,
-77,,
20,,
-82,,
3,,
-146,,
19,,
24,,
25,,
30,,
-70,,
62,,
-33,,
-115,,
-133,,
-84,,
40,,
-141,,
-115,,
75,,
17,,
-14,,
-92,,
59,,
-9,,
-10,,
7,,
-48,,
38,,
-73,,
-31,,
-77,,
-61,,
-117,,
4,,
-100,,
85,,
-131,,
-17,,
-101,,
-107,,
-145,,
16,,
86,,
17,,
0,,
80,,
-79,,
30,,
-12,,
84,,
56,,
37,,
97,,
-58,,
-145,,
84,,
48,,
-95,,
-36,,
-60,,
-130,,
-8,,
80,,
81,,
-14,,
67,,
-17,,
93,,
18,,
-70,,
-10,,
-54,,
-61,,
-27,,
92,,
75,,
-41,,
91,,
13,,
91,,
7,,
-94,,
-8,,
-5,,
-119,,
64,,
65,,
11,,
-63,,
-38,,
-17,,
41,,
-84,,
-4,,
-24,,
-119,,
18,,
-123,,
-79,,
-135,,
-105,,
75,,
-20,,
-59,,
-98,,
-124,,
-135,,
-107,,
-135,,
86,,
-11,,
85,,
-90,,
-55,,
-89,,
34,,
-91,,
76,,
-2,,
-116,,
-12,,
-12,,
-117,,
-24,,
-73,,
53,,
89,,
45,,
-147,,
-3,,
92,,
-105,,
-90,,
78,,
18,,
-132,,
2,,
82,,
-138,,
-103,,
-64,,
29,,
-65,,
52,,
85,,
-75,,
15,,
-42,,
-11,,
-105,,
72,,
20,,
-103,,
-111,,
46,,
-131,,
-69,,
83,,
-120,,
-131,,
-39,,
-33,,
57,,
19,,
-4,,
-126,,
25,,
-106,,
72,,
39,,
63,,
-138,,
58,,
59,,
-110,,
-2,,
40,,
-35,,
58,,
-137,,
28,,
69,,
-115,,
-138,,
-78,,
-35,,
-123,,
64,,
-104,,
-97,,
97,,
48,,
-93,,
78,,
79,,
-25,,
-7,,
-81,,
52,,
-88,,
94,,
-73,,
-3,,
49,,
-104,,
-148,,
-45,,
-15,,
17,,
-76,,
-40,,
-114,,
51,,
-107,,
-44,,
-117,,
41,,
42,,
27,,
2,,
-106,,
53,,
4,,
-77,,
51,,
-116,,
-136,,
-146,,
-98,,
7,,
-136,,
73,,
33,,
91,,
-57,,
-106,,
59,,
-134,,
77,,
-36,,
49,,
-59,,
-31,,
-47,,
39,,
-39,,
35,,
-22,,
-127,,
-107,,
0,,
-132,,
17,,
57,,
-88,,
-53,,
31,,
-142,,
-101,,
63,,
-69,,
-119,,
66,,
-43,,
-6,,
-9,,
-127,,
71,,
-86,,
85,,
-27,,
51,,
-128,,
-41,,
38,,
-58,,
63,,
35,,
-147,,
-77,,
-111,,
-80,,
32,,
-101,,
-22,,
-85,,
18,,
-83,,
-145,,
82,,
94,,
56,,
-98,,
29,,
85,,
-117,,
-16,,
-73,,
49,,
-123,,
-64,,
-74,,
-1,,
39,,
-129,,
-92,,
-21,,
6,,
59,,
-57,,
-49,,
73,,
52,,
-19,,
-110,,
-112,,
-118,,
77,,
80,,
-144,,
-58,,
-28,,
-76,,
53,,
-16,,
-136,,
11,,
-76,,
-71,,
93,,
25,,
-87,,
35,,
-7,,
50,,
51,,
-48,,
-97,,
40,,
-16,,
-94,,
-45,,
90,,
-1,,
20,,
88,,
-134,,
-104,,
-150,,
62,,
42,,
-142,,
-146,,
-94,,
-147,,
-122,,
-5,,
56,,
76,,
39,,
-86,,
84,,
-23,,
-104,,
-3,,
-85,,
-106,,
-127,,
-88,,
49,,
33,,
45,,
79,,
47,,
-25,,
-84,,
-66,,
70,,
-142,,
-51,,
-92,,
-75,,
-118,,
73,,
-129,,
-48,,
43,,
64,,
27,,
-82,,
-72,,
-149,,
2,,
-144,,
-114,,
7,,
69,,
21,,
-69,,
-10,,
-8,,
-91,,
69,,
31,,
-48,,
-128,,
-39,,
-14,,
86,,
25,,
16,,
-10,,
-120,,
38,,
-66,,
8,,
5,,
-125,,
-26,,
-48,,
21,,
86,,
-15,,
38,,
-133,,
-4,,
-85,,
-12,,
-47,,
-23,,
-115,,
-149,,
-109,,
-69,,
5,,
48,,
78,,
-56,,
96,,
46,,
-127,,
-79,,
93,,
-66,,
-97,,
-127,,
88,,
-111,,
6,,
75,,
-126,,
-63,,
23,,
70,,
-60,,
-39,,
25,,
51,,
75,,
-15,,
-131,,
-82,,
-13,,
-87,,
0,,
20,,
-117,,
-34,,
-111,,
-142,,
-9,,
-98,,
53,,
0,,
24,,
-112,,
-25,,
-145,,
-80,,
-113,,
16,,
57,,
-111,,
79,,
-77,,
36,,
13,,
22,,
-146,,
-15,,
-41,,
63,,
61,,
-142,,
-9,,
35,,
-13,,
-129,,
62,,
-143,,
-113,,
-125,,
52,,
91,,
94,,
31,,
36,,
40,,
-122,,
79,,
78,,
-56,,
86,,
62,,
-14,,
-119,,
71,,
-21,,
-57,,
-34,,
23,,
-80,,
-92,,
-146,,
-56,,
33,,
-33,,
-99,,
-76,,
-65,,
97,,
-53,,
-107,,
-30,,
-68,,
-29,,
-12,,
-107,,
-71,,
12,,
-19,,
16,,
-129,,
-22,,
-97,,
49,,
-78,,
-116,,
-25,,
-91,,
71,,
-64,,
-139,,
-105,,
-52,,
-9,,
-24,,
-82,,
46,,
-9,,
-56,,
-70,,
-63,,
-96,,
-83,,
34,,
-92,,
91,,
-140,,
-31,,
-79,,
-110,,
7,,
20,,
64,,
-56,,
-15,,
-84,,
-122,,
25,,
-108,,
-11,,
81,,
-58,,
-83,,
-19,,
15,,
-12,,
-11,,
-42,,
-5,,
96,,
-63,,
-29,,
64,,
-108,,
-32,,
-107,,
-141,,
-17,,
42,,
-105,,
-110,,
-118,,
-99,,
-70,,
-37,,
-93,,
-140,,
-36,,
90,,
-149,,
60,,
-81,,
26,,
-63,,
83,,
32,,
-65,,
80,,
1,,
90,,
-84,,
-132,,
-72,,
-149,,
3,,
-147,,
-85,,
-80,,
38,,
-3,,
-107,,
-79,,
-121,,
-87,,
79,,
-85,,
-23,,
-61,,
-59,,
-128,,
-28,,
-67,,
-65,,
-52,,
67,,
37,,
-89,,
42,,
17,,
88,,
93,,
75,,
-1,,
-60,,
-107,,
-62,,
55,,
-47,,
-36,,
-121,,
-94,,
-57,,
-45,,
-100,,
83,,
67,,
97,,
-89,,
-6,,
-139,,
93,,
-132,,
-125,,
-118,,
-114,,
-75,,
-87,,
-134,,
-11,,
-103,,
-71,,
57,,
-148,,
-24,,
-56,,
-66,,
-119,,
-8,,
-22,,
-74,,
-63,,
96,,
-114,,
53,,
80,,
-3,,
-98,,
-150,,
-104,,
-12,,
-41,,
-75,,
-40,,
30,,
49,,
18,,
-41,,
64,,
95,,
74,,
-27,,
97],
listLength = len(numbers),
total = 0,
,
for i in numbers:,
    total += i,
,
final = total/listLength,
final = str(round(final, 2)),
print(final),