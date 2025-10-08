# page_replacement.py
# Лаборатория: Жадты басқару және виртуалды жады
# Тақырып: FIFO және LRU алгоритмдері

page_refs = [1, 2, 3, 1, 4, 5, 1, 2, 3, 4, 5]
frames_count = 4

# FIFO Алгоритмі
def fifo(pages, frames_count):
    frames = []
    faults = 0
    for page in pages:
        if page not in frames:
            faults += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
        print(f"FIFO: {frames}")
    return faults

# -------- LRU Алгоритмі --------
def lru(pages, frames_count):
    frames = []
    faults = 0
    recent = []
    for page in pages:
        if page not in frames:
            faults += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                # ең сирек қолданылғанды шығарамыз
                lru_page = recent[0]
                frames[frames.index(lru_page)] = page
        # қолданылу реті
        if page in recent:
            recent.remove(page)
        recent.append(page)
        print(f"LRU: {frames}")
    return faults

fifo_faults = fifo(page_refs, frames_count)
lru_faults = lru(page_refs, frames_count)

print("\nНәтиже:")
print("FIFO бет қателігі:", fifo_faults)
print("LRU бет қателігі:", lru_faults)

# Талдау:
if fifo_faults > lru_faults:
    print("LRU тиімдірек, себебі ол жиі қолданылатын беттерді ұстап қалады.")
elif fifo_faults < lru_faults:
    print("FIFO тиімдірек, бірақ бұл сирек болады.")
else:
    print("Екеуі де бірдей тиімді болды.")
