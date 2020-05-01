import math
import nltk
import numpy as np
import torch

def bleu_eval(encoder, decoder, data_loader, batch_size, device):
    with torch.no_grad():
        true_outputs = [] # e.g: [[ref1_1, ref1_2], [ref2_1, ...], ....]
        decoder_outputs = [] # e.g: [out1, out2, out3]
        for i, (images, captions, lengths) in enumerate(data_loader):
<<<<<<< HEAD
            
=======

            if i > 0:
                break
            if i * batch_size >= 10000 or len(images) != batch_size:
                continue
>>>>>>> 6a1c3b988787b8cb079b846922e634a51dcde603
            for caption in captions:
                caption = caption.numpy().astype(str).tolist()
                idx = 0
                curr_img_captions = [[]] # e.g: [ref1_1, ref1_2, ...]
                for tok in caption[1:-1]:
                    if tok == '4': # '<break>'
                        idx += 1
                        curr_img_captions.append([])
                    elif tok != '0': # '<pad>'
                        curr_img_captions[idx].append(tok)
                true_outputs.append(curr_img_captions)

            images = images.to(device)
            captions = captions.to(device)

            features = encoder(images)
<<<<<<< HEAD
            max_sequence_length = int(np.array(captions != 0).sum(axis = 1).mean()+1)
=======
            outputs = decoder(features, captions, lengths)
>>>>>>> 6a1c3b988787b8cb079b846922e634a51dcde603
            sample = decoder.sample(features, max_seq_length=20).cpu()
            decoder_outputs.extend(sample.numpy().astype(str).tolist())

        predictions = []
        for pred in decoder_outputs:
            curr = []
            for tok in pred:
                if tok == '2': # '<end>'
                    break
                curr.append(tok)
            predictions.append(curr)
        return predictions, nltk.bleu_score.corpus_bleu(true_outputs, predictions, weights=(0.33, 0.33, 0.33, 0.0))
