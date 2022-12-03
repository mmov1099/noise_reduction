import seaborn as sns
import matplotlib.pyplot as plt

def plot_data(data, timestamp, mask=False):
    if mask is False:
        mask=data==1.0000000e+04
    fig, ax = plt.subplots(figsize=(10,2))
    sns.heatmap(data, cmap="jet", mask=mask, vmax=500 ,vmin=-500)
    ax.invert_yaxis()
    ax.set(ylabel='rgate_no_1')
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
    ax.collections[0].colorbar.set_label('Doppler velocity[m/s]')
    ax.set(xticklabels=[])
    # ax[0].tick_params(bottom=False)
    idxs = [int(xtick) for xtick in ax.get_xticks()]
    xlabels = [timestamp[idx] for idx in idxs]
    ax.set_xticklabels(xlabels)
    ax.set(xlabel='epoch')
    plt.subplots_adjust(hspace=0.08)
    plt.show()

def plot_list_data(list_data, timestamp, mask_value=False):
    fig, ax = plt.subplots(len(list_data), sharey='all', figsize=(10,2*len(list_data)))
    for i, d in enumerate(list_data):
        if mask_value is False:
            mask=d==1.0000000e+04
        else:
            mask=d>=mask_value
        sns.heatmap(d, ax=ax[i], cmap="jet", mask=mask, vmax=500 ,vmin=-500)
        ax[i].invert_yaxis()
        ax[i].set(ylabel='rgate_no_1')
        ax[i].spines['right'].set_visible(True)
        ax[i].spines['top'].set_visible(True)
        ax[i].spines['left'].set_visible(True)
        ax[i].spines['bottom'].set_visible(True)
        ax[i].collections[0].colorbar.set_label('Doppler velocity[m/s]')
        ax[i].set(xticklabels=[])
        # ax[i].tick_params(bottom=False)
    idxs = [int(xtick) for xtick in ax[-1].get_xticks()]
    xlabels = [timestamp[idx] for idx in idxs]
    ax[-1].set_xticklabels(xlabels)
    ax[-1].set(xlabel='epoch')
    plt.subplots_adjust(hspace=0.08)
    plt.show()