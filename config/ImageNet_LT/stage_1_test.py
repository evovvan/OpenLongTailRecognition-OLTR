# Testing configurations
config = {}

training_opt = {}
training_opt['dataset'] = 'ImageNet_LT'
training_opt['log_dir'] = './logs/ImageNet_LT/stage1'
training_opt['num_classes'] = 1000
training_opt['batch_size'] = 128
training_opt['num_workers'] = 4
training_opt['num_epochs'] = 1
training_opt['display_step'] = 10
training_opt['feature_dim'] = 512
training_opt['open_threshold'] = 0.1
training_opt['sampler'] = {'type': 'ClassAwareSampler', 'def_file': './data/ClassAwareSampler.py',
                           'num_samples_cls': 4}
training_opt['scheduler_params'] = {'step_size':10, 'gamma':0.1}
config['training_opt'] = training_opt

networks = {}
feature_param = {'use_selfatt':False, 'use_fc': True, 'dropout': None,
			  'stage1_weights': False, 'dataset': training_opt['dataset'], 'caffe': False}
feature_optim_param = {'lr': 0.01, 'momentum':0.9, 'weight_decay':0.0005}
networks['feat_model'] = {'def_file': './models/ResNet10Feature.py',
                          'params': feature_param,
                          'optim_params': feature_optim_param,
                          'fix': False}
classifier_param = {'in_dim': training_opt['feature_dim'], 'num_classes': training_opt['num_classes'],
				'stage1_weights': False, 'dataset': training_opt['dataset']}
classifier_optim_param = {'lr': 0.1, 'momentum':0.9, 'weight_decay':0.0005}
networks['classifier'] = {'def_file': './models/DotProductClassifier.py',
                          'params': classifier_param,
                          'optim_params': classifier_optim_param}
config['networks'] = networks

criterions = {}
perf_loss_param = {}
criterions['PerformanceLoss'] = {'def_file': './loss/SoftmaxLoss.py', 'loss_params': perf_loss_param,
                                 'optim_params': None, 'weight': 1.0}
config['criterions'] = criterions

relations = {}
relations['centers'] = False
relations['init_centers'] = False
config['relations'] = relations

