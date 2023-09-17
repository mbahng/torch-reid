import torchreid

print(torchreid.models.show_avai_models())

print(train_sampler)
# datamanager = torchreid.data.ImageDataManager(
#     root='reid-data',
#     sources='market1501',
#     targets='dukemtmcreid', # or targets='cuhk03' or targets=['dukemtmcreid', 'cuhk03']
#     height=256,
#     width=128
# )